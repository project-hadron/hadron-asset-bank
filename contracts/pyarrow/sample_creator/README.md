# Sample Creator
Takes an input datasets and produces a sample dataset randomly selected.

### General Environment Variables
Create the environment variables.
* HADRON_DOMAIN_REPO_PATH - the location path of the Hadron Controller and its component capabilities.

### Component Specific Environment Variables
The following environment variables are specific to the Sample Creator.
* HADRON_SAMPLE_SIZE - The size of the sample to take from the dataset.
* HADRON_SOURCE_URI - The full URI of the location of the source dataset.
* HADRON_PERSIST_URI - The full URI of the sample dataset.

## Hadron docker-compose example
 an example yaml file skeleton might look like.

```yaml
version: '3.8'
services:
  domain-controller:
    image: gigas64/hadron_pyarrow:latest
    env_file: private_env_file
    environment:
      # mandatory domain ensemble path
      HADRON_DOMAIN_REPO_PATH: 
      # specific component envs
      HADRON_SAMPLE_SIZE: 5000
      HADRON_SOURCE_URI: s3://bucket/path/source.csv
      HADRON_PERSIST_URI: ./path/sample.parquet
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
