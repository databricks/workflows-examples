# dbt Packages demo

Example showing different dbt packages that can be used to speed up and improve the dbt and Databricks development workflow

## Add spark_utils to packages and project

In the packgages file add

```
packages:
  - package: dbt-labs/spark_utils
    version: 0.3.0
```

In the dbt_project.yml file add

```
dispatch:
  - macro_namespace: dbt_utils
    search_order: ['spark_utils', 'dbt_utils']
```