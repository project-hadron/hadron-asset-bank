To run the controller in a `Cortex` `Domain Contract Executor` skill pass the following dictionary as a payload

```python
{
    "domain_contract_repo":"https://raw.githubusercontent.com/project-hadron/hadron-asset-bank/master/contracts/helloworld/feature_catalog/profile_features",
    "hadron_kwargs":{
        "HADRON_DEFAULT_PATH":"s3://project-hadron-cs-repo/domain/helloworld/data/feature_catalog/profile_features/",
        "HADRON_DATALAKE_VERSION": "v08"
    }
}
```

The `domain_contract_repo` is a mandatory key and point to the `Domain Contract` for this run.

The `hadron_kwargs` are a set of optional parameters to pass to the controller. In this instance we are:
- `HADRON_DEFAULT_PATH` - path where we wish all data output to be placed.
- `HADRON_DATALAKE_VERSION` - The version number of the synthetic build SoR 
