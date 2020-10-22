"""Airflow DAG - Data ingestion ELT (Extract-Load-Transform) process with Apache Airflow"""
from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

__author__ = "Ebube Abara"
__copyright__ = "Ebube Abara"
__version__ = "1.0"
__maintainer__ = "Ebube Abara"
__email__ = "ebubeabara3@gmail.com"
__status__ = "Development"

dag_id = 'data-ingestion'
dag_description = 'Data ingestion ELT (Extract-Load-Transform) process with Apache Airflow'

data_path = '/root/jobs/data-integration-with-apache-airflow'  # replace with your directory path
src_path = '/root/jobs/data-integration-with-apache-airflow/src'  # replace with directory path

url = 'https://introcs.cs.princeton.edu/java/data/pizzahut.csv'
absolute_path = f'{data_path}/pizzahut.csv'
db_connection_string = f'{data_path}/pizzahut.db'

script_extract_and_load_to_data_lake = f'{src_path}/extract_and_load_to_data_lake.py'
script_transform_from_data_lake_to_database = f'{src_path}/transform_from_data_lake_to_database.py'

default_args = {
    'owner': 'Ebube Abara',
    'depends_on_past': False,
    'retries': 5,
    'retry_delay': timedelta(seconds=15)
}

dag = DAG(
    dag_id=dag_id,
    schedule_interval='0 0 * * *',  # run daily at midnight
    start_date=datetime(2020, 10, 21),
    catchup=False,
    default_args=default_args,
    description=dag_description,
    max_active_runs=1
)

extract_and_load_to_data_lake = BashOperator(
    task_id='extract_and_load_to_data_lake',
    dag=dag,
    bash_command=f'bin/sh;python3 {script_extract_and_load_to_data_lake} {url} {absolute_path};'
)

transform_from_data_lake_to_database = BashOperator(
    task_id='transform_from_data_lake_to_database',
    dag=dag,
    bash_command=f'bin/sh;python3 {script_transform_from_data_lake_to_database} {absolute_path} {db_connection_string};'
)

extract_and_load_to_data_lake >> transform_from_data_lake_to_database
