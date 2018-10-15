# UnitTest


## Files structure
`airflow unittest` working dir is ./unittest:

File and Directory inside:

* `airflow/Dockerfile` airflow env build Dockerfile that include all airflow project bin command and dependence
* `data` Temp file directory
* `opt` script, data and logs directory
	* `airflow_start.sh` airflow init and start script
	* `main_test.py` airflow payload init program and airflow task run main
	* `wait-for-it.sh` script to monitor mysql is ready

* `docker-compose.yml` docker compose file to up and startup unit test

## How to run
### Fullfill business payload 
in File `main_test.py`

```python
ele_desc = {}
payload = {'element': ele_desc}
dag_id = 'dag_id'
task_id = 'task_id'
dag_file_path = 'dag_file_path'
```

## How to remote debug
* add debug code in file `/root/miniconda3/bin/airflow`
	
	```python
	import pydevd
	pydevd.settrace('host.docker.internal', port=54321, stdoutToServer=True, stderrToServer=True)
	```
* PyCharm
* confirm what all projects need are avaliable in Python Path, like `airflow`, `submarine-datacenter` and so on
* create remote debug server in PyCharm with hostname `localhost` and port `54321`, then start
* then docker-compose up


