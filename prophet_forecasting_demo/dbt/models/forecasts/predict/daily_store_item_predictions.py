from pyspark.sql.types import *
from pyspark.sql.functions import current_date
import pandas as pd
from prophet import Prophet, serialize


def forecast_store_item( history_pd: pd.DataFrame ) -> pd.DataFrame:
  
  # TRAIN MODEL AS BEFORE
  # --------------------------------------
  # remove missing values (more likely at day-store-item level)
  history_pd = history_pd.dropna()
  
  # configure the model
  model = Prophet(
    interval_width=0.95,
    growth='linear',
    daily_seasonality=False,
    weekly_seasonality=True,
    yearly_seasonality=True,
    seasonality_mode='multiplicative'
    )
  
  # train the model
  model.fit( history_pd )
  # --------------------------------------
  
  # BUILD FORECAST AS BEFORE
  # --------------------------------------
  # make predictions
  future_pd = model.make_future_dataframe(
    periods=90, 
    freq='d', 
    include_history=True
    )
  forecast_pd = model.predict( future_pd )  
  # --------------------------------------
  
  # ASSEMBLE EXPECTED RESULT SET
  # --------------------------------------
  # get relevant fields from forecast
  f_pd = forecast_pd[ ['ds','yhat', 'yhat_upper', 'yhat_lower'] ].set_index('ds')
  
  # get relevant fields from history
  h_pd = history_pd[['ds','store','item','y']].set_index('ds')
  
  # join history and forecast
  results_pd = f_pd.join( h_pd, how='left' )
  results_pd.reset_index(level=0, inplace=True)
  
  # get store & item from incoming data set
  results_pd['store'] = history_pd['store'].iloc[0]
  results_pd['item'] = history_pd['item'].iloc[0]
  # --------------------------------------
  
  # return expected dataset
  return results_pd[ ['ds', 'store', 'item', 'y', 'yhat', 'yhat_upper', 'yhat_lower'] ]  

def model(dbt, session):
    dbt.config(
      materialized="table",
      packages = ["numpy==1.23.1", "scikit-learn", "prophet==1.1.1"]
    )

    # DataFrame representing an upstream model
    store_sales_df = dbt.ref("daily_store_item_prep")

    # Cache the data 
    store_item_history = (
      store_sales_df.repartition(sc.defaultParallelism, ['store', 'item'])
    ).cache()

    result_schema =StructType([
      StructField('ds',DateType()),
      StructField('store',IntegerType()),
      StructField('item',IntegerType()),
      StructField('y',FloatType()),
      StructField('yhat',FloatType()),
      StructField('yhat_upper',FloatType()),
      StructField('yhat_lower',FloatType())
    ])

    results_df = (
      store_item_history
        .groupBy('store', 'item')
          .applyInPandas(forecast_store_item, schema=result_schema)
        .withColumn('training_date', current_date() )
      )
    results_renamed_df = (
      results_df.withColumnRenamed('ds','date')
      .withColumnRenamed('y','sales')
      .withColumnRenamed('yhat','sales_predicted')
      .withColumnRenamed('yhat_upper','sales_predicted_upper')
      .withColumnRenamed('yhat_lower','sales_predicted_lower')
    )
    return results_renamed_df