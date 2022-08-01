# Marketing Analytics Demo

This folder contains the Databricks Workflows job configuration and the dbt project for the Databricks Marketing Analytics with Fivetran and dbt blog post.

## Setting up dbt project in a Databricks Workflows job via the UI

Fork this repo and create a Databricks Workflows job pointing to the repo with 2 tasks

Task 1 should run the dbt commands:
- dbt deps
- dbt run

Task 2 should run the dbt command:
- dbt test

Task 2 should depend on task 1.

Full steps are shown in the blog post.

## Setting dbt project in a Databricks Workflows job using CLI or API

Use the Workflows [create-job.json](/workflows/create-job.json) configuration to set-up the job using one of the following:

- [dbx](https://dbx.readthedocs.io/en/latest/guidance/multitask_jobs.html#sample-multitask-jobs-based-on-jobs-api-2-1)
- [Databricks Jobs CLI](https://docs.databricks.com/dev-tools/cli/jobs-cli.html#create-a-job)
- [Jobs 2.1 API](https://docs.databricks.com/dev-tools/api/latest/jobs.html#operation/JobsCreate)


## Setting up dbt project with dbt Core or dbt Cloud

Follow the instructions for setting up dbt and Databricks:

- [dbt Core](https://docs.databricks.com/integrations/prep/dbt.html)
- [dbt Cloud](https://docs.databricks.com/integrations/prep/dbt-cloud.html)

Fork and git clone this repo locally to use with dbt Core or create a [GitHub connection in dbt Cloud](https://docs.getdbt.com/docs/dbt-cloud/cloud-configuring-dbt-cloud/cloud-installing-the-github-application)

Run the commands:

- dbt deps
- dbt run
- dbt test



