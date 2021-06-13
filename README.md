# Example ETL job using Python
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-360/)
This example ETL jobs scrapes data from `azair.com`, formulates records and saves them into the SQLite database.

!["ETL"](./images/etl.png)

## Requirements

1. [Docker](https://www.docker.com/)


## Run ETL job
You can use optional parameter with tag version. (eg. `v0.1`)
1. Build docker image
```sh
./build.sh
```

2. Run docker image
```sh
./run.sh
```


## Run tests

```sh
pytest --show-capture=no 
```