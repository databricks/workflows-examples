with forecast_prep as (

  select
      store,
      item,
      CAST(date as date) as ds,
      SUM(sales) as y
  from {{ ref('store_item_sales') }}
    group by store, item, ds
    order by store, item, ds

)

select *
from forecast_prep