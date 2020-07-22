# Example ETL job using Python

This example ETL jobs scrapes data from `azair.com`, formulates records and saves them into the SQLite database.

!["ETL"](./images/etl.png)

## Requirements

1. Python 3.7+ - [link](https://www.python.org/)


## Run ETL job

1. Create virtual enviroment - [link](https://docs.python.org/3/library/venv.html).

2. Run below command:
```sh
pip install -r requirements.txt
```
3. Run job:
```sh
./run_etl_job.sh
```

## Run tests

```sh
./run_unit_tests.sh
```