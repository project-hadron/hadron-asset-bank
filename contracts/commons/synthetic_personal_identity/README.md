# Synthetic Data Types Component Service
Synthetically generates a dataset of Personal Identity Information (PII) with patterns to test the robustness
of ingesting systems or solutions. The dataset has 13 columns.

### General Environment Variables
Create the environment variables
* HADRON_DOMAIN_REPO_PATH - the location path of the Hadron Controller and its component capabilities

### Component Specific Environment Variables
The following environment variables are specific to this Difference Report
* HADRON_SYNTHETIC_DATA_SIZE - The size, in rows, of the dataset.
* HADRON_SYNTHETIC_OUTCOME_URI - the full output uri for the resulting dataset

## Hadron docker-compose example
 an example yaml file might look like

```yaml
version: '3.8'
services:
  domain-controller:
    image: gigas64/project_hadron:3.4
    env_file: credential_file
    environment:
      # mandatory domain ensemble path
      - HADRON_DOMAIN_REPO_PATH=https://raw.githubusercontent.com/project-hadron/hadron-asset-bank/master/contracts/commons/synthetic_personal_identity
      # specific component envs
      - HADRON_SYNTHETIC_DATA_SIZE=1000
      - HADRON_SYNTHETIC_OUTCOME_URI=/data/cache/data/hadron_synthetic_data_types.parquet
    volumes:
      - ./cache:/data/cache
      - ~/.aws/credentials:/root/.aws/credentials:ro

```
where the `private_env_file` contains private environment variables such as connector secrets or tokens and
the `gigas64/project_hadron:latest` image is the generic docker image to run Project Hadron Component Services.

If you are not using thr `credential_file` then remove the `env_file:` entry

Then to start the docker container, from the location of your `docker-compose.yml` file, run
```bash
$> docker-compose up -d
```

To stop the docker container, run
```bash
$> docker-compose down
$> docker-compose stop
```
