# Data Profiling Component Service
Takes an input datasets, produces a set of data profiling.

### General Environment Variables
Create the environment variables
* HADRON_DOMAIN_REPO_PATH - the location path of the Hadron Controller and its component capabilities
* HADRON_DEFAULT_PATH - a default path where to put non-specified outputs.

### Component Specific Environment Variables
The following environment variables are specific to the Data Profiling Report
* HADRON_PROFILING_SOURCE_URI - The full URI of the dataset to be data profiled.
* HADRON_DATA_QUALITY_URI - The full URI of where to put data quality report
* HADRON_DATA_DICTIONARY_URI - The full URI of where to put data dictionary report
* HADRON_DATA_SCHEMA_URI - The full URI of where to put data schema report

## Hadron docker-compose example
 an example yaml file skeleton might look like

```yaml
version: '3.8'
services:
  domain-controller:
    image: gigas64/hadron_pyarrow:1.0
    env_file: private_env_file
    environment:
      # mandatory domain ensemble path
      HADRON_DOMAIN_REPO_PATH: 
      # controller startup envs (optional)
      HADRON_CONTROLLER_REPORT: 
      # Connector contract paths (optional)
      HADRON_DEFAULT_PATH: 
      # specific component envs
      HADRON_PROFILING_SOURCE_URI: 
      HADRON_DATA_QUALITY_URI: 
      HADRON_DATA_DICTIONARY_URI: 
      HADRON_DATA_SCHEMA_URI: 
    volumes:
      - ./cache:/data/cache
      - ~/.aws/credentials:/root/.aws/credentials:ro
```
where the `private_env_file` contains private environment variables such as connector secrets or tokens and
the `gigas64/project_hadron:2.1` image is the generic docker image to run Project Hadron Component Services.

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
