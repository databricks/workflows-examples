# Marketing Analytics Demo

This folder contains the dbt project for the Databricks Marketing Analytics with Fivetran and dbt blog post.

## Using the dbt project in Databricks Workflows

Fork this repo and create a Databricks Workflows job pointing to the repo with 2 tasks

Task 1 should run the dbt commands:
- dbt deps
- dbt run

Task 2 should run the dbt command:
- dbt test

## Using with dbt Core or dbt Cloud

Follow the instructions for setting up dbt and Databricks:

- [dbt Core](https://docs.databricks.com/integrations/prep/dbt.html)
- [dbt Cloud](https://docs.databricks.com/integrations/prep/dbt-cloud.html)

Then fork and git clone this repo locally or create a connection in dbt Cloud



