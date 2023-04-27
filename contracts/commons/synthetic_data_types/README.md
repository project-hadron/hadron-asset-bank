# Synthetic Data Types Component Service
Synthetically generates a dataset of different data types and patterns to test the robustness of ingesting 
systems or solutions. The dataset has 27 columns.

### General Environment Variables
Create the environment variables
* HADRON_DOMAIN_REPO_PATH - the location path of the Hadron Controller and its component capabilities

### Component Specific Environment Variables
The following environment variables are specific to this Difference Report
* HADRON_SYNTHETIC_DATA_SIZE - The size, in rows, of the dataset.
* HADRON_SYNTHETIC_DATA_TYPES_URI - the output uri for the results

## Hadron docker-compose example
 an example yaml file skeleton might look like

```yaml
version: '3.8'
services:
  domain-controller:
    image: gigas64/project_hadron:3.4
    env_file: credential_env
    environment:
      # mandatory domain ensemble path
      - HADRON_DOMAIN_REPO_PATH=https://raw.githubusercontent.com/project-hadron/hadron-asset-bank/master/contracts/commons/synthetic_data_types
      # specific component envs
      - HADRON_SYNTHETIC_DATA_SIZE=1000
      - HADRON_SYNTHETIC_DATA_TYPES_URI=/data/cache/data/hadron_synthetic_data_types.parquet
    volumes:
      - ./cache:/data/cache
```
where the `private_env_file` contains private environment variables such as connector secrets or tokens and
the `gigas64/project_hadron:latest` image is the generic docker image to run Project Hadron Component Services.

Then to start run
```bash
$> docker-compose up
```