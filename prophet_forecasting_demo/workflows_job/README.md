# Workflows Job 

## Create using CLI or API using JSON

```
{
    "creator_user_name": "user@company.com",
    "run_as_user_name": "user@company.com",
    "run_as_owner": true,
    "settings": {
        "name": "dbt demo - store sales predictions workflow ",
        "email_notifications": {
            "no_alert_for_skipped_runs": false
        },
        "timeout_seconds": 0,
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "task_key": "ingest_csv",
                "notebook_task": {
                    "notebook_path": "/Repos/user@company.com/workflow-examples/notebooks/ingest-sales-csv-to-delta",
                    "source": "WORKSPACE"
                },
                "existing_cluster_id": "1005-133139-6fgraiod",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "dbt_model",
                "depends_on": [
                    {
                        "task_key": "ingest_csv"
                    }
                ],
                "dbt_task": {
                    "project_directory": "prophet_forecasting_demo/dbt/",
                    "commands": [
                        "dbt debug",
                        "dbt run"
                    ],
                    "profiles_directory": ""
                },
                "job_cluster_key": "dbt_CLI",
                "libraries": [
                    {
                        "pypi": {
                            "package": "dbt-databricks==1.3.0b0"
                        }
                    }
                ],
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "dashboard_refresh",
                "depends_on": [
                    {
                        "task_key": "dbt_model"
                    }
                ],
                "sql_task": {
                    "dashboard": {
                        "dashboard_id": "4dcdd90d-1a51-42c4-aeca-806087c172db"
                    },
                    "warehouse_id": "61cc274d10838ee5"
                },
                "timeout_seconds": 0,
                "email_notifications": {}
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "dbt_CLI",
                "new_cluster": {
                    "spark_version": "10.4.x-scala2.12",
                    "spark_conf": {
                        "spark.master": "local[*, 4]",
                        "spark.databricks.cluster.profile": "singleNode"
                    },
                    "aws_attributes": {
                        "first_on_demand": 1,
                        "availability": "SPOT_WITH_FALLBACK",
                        "zone_id": "us-west-2b",
                        "spot_bid_price_percent": 100,
                        "ebs_volume_count": 0
                    },
                    "node_type_id": "i3.xlarge",
                    "custom_tags": {
                        "ResourceClass": "SingleNode"
                    },
                    "spark_env_vars": {
                        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
                    },
                    "enable_elastic_disk": true,
                    "data_security_mode": "SINGLE_USER",
                    "runtime_engine": "STANDARD",
                    "num_workers": 0
                }
            }
        ],
        "git_source": {
            "git_url": "https://github.com/databricks/workflows-examples",
            "git_provider": "gitHub",
            "git_branch": "dbt_python_forecast"
        },
        "format": "MULTI_TASK"
    }
}
```

