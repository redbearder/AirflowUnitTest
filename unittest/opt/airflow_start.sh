#!/usr/bin/env bash
apt install -y mysql-client

rm -Rf ~/airflow
cp -Rf /airflow ~/airflow
cp ~/airflow/airflow.unittest.cfg ~/airflow/airflow.cfg

mysql -h mysql -uroot -proot -e "CREATE DATABASE IF NOT EXISTS airflow DEFAULT CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;"

airflow resetdb -y 
airflow initdb 
airflow pool -s DRAW_TASKS 2 "pool for drawers" 
# airflow webserver -p 8080 &
# airflow scheduler &

python /opt/main_test.py