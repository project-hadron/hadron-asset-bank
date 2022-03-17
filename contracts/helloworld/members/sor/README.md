To run the controller in a `Cortex` `Domain Contract Executor` skill pass the following dictionary as a payload

```python
{
    "hadron_kwargs":{
            "HADRON_ROW_SIZE": 10000,
            "HADRON_FEEDBACK_PATH": "s3://project-hadron-cs-repo/10/2022-03-16 20:49:07.602028/members_feedback_v16.parquet",
            "HADRON_MEMBERS_PATH": "s3://project-hadron-cs-repo/10/2022-03-16 20:49:07.602028/members_v14.parquet",
            "HADRON_FLU_RISK_PATH": "s3://project-hadron-cs-repo/10/2022-03-16 20:49:07.602028/members_flu_risk_v14.parquet"
        },
    "domain_contract_repo": "https://raw.githubusercontent.com/project-hadron/hadron-asset-bank/master/contracts/helloworld/members/sor"
}
```

The `domain_contract_repo` is a mandatory key and point to the `Domain Contract` for this run.

The `hadron_kwargs` are a set of optional parameters to pass to the controller. In this instance we are:
- `HADRON_ROW_SIZE` - the Size of the data we want to generate
- `HADRON_FEEDBACK_PATH` - Path to save Feedback data
- `HADRON_MEMBERS_PATH` - Path to save Members data
- `HADRON_FLU_RISK_PATH` - Path to save Flu risk data
