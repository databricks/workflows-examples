# Prophet Forecasting Demo

This demo shows how to create a Databricks Workflows Job that has 3 tasks

- Ingest Store Item Sales CSV file into Delta Lake
- Run a dbt model as a task to transform and run forcasting predictions
- Update a Databricks SQL dashboard showing the predictions