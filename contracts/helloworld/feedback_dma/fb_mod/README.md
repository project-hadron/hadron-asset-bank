To run the controller in a `Cortex` `Domain Contract Executor` skill pass the following dictionary as a payload

```python
{
    "domain_contract_repo":"https://raw.githubusercontent.com/project-hadron/hadron-asset-bank/master/contracts/helloworld/feedback_dma/fb_mod",
    "hadron_kwargs":{
        "HADRON_DEFAULT_PATH":"s3://project-hadron-cs-repo/domain/helloworld/data/feedback_dma/fb_mod/",
        "HADRON_CAMPAIGN_WATCHLIST":"hw-campaign-im-48fac_watchlist.parquet"
    }
}
```

The `domain_contract_repo` is a mandatory key and point to the `Domain Contract` for this run.

The `hadron_kwargs` are a set of optional parameters to pass to the controller. In this instance we are:
- `HADRON_DEFAULT_PATH` - path where we wish all data output to be placed.
- `HADRON_CAMPAIGN_WATCHLIST` - The uri where the Watchlist can be located 
