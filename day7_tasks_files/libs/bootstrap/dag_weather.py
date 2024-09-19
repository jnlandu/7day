from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from utils.weather_utils import get_weather_data, API_KEY
# from  code.weather_utils import get_weather_data

from airflow.models import Variable


# WEATHER_API = Variable.get('WEATHER_API_KEY_SECRET')
# ACCSESS_KEY_ID = Variable.get('AWS_ACCSESS_KEY_ID_SECRET')
# SECRET_ACCESS_KEY = Variable.get('AWS_SECRET_ACCESS_KEY')

default_args = {
    "start_date":datetime(2023, 8, 11),
    "retries":10,
    "retry_delay":timedelta(minutes=15)
}


with DAG('dag_weather', schedule_interval='59 16 * * *', default_args=default_args, catchup=False, tags=['weather']) as dag3:
    
    retrieve_data = PythonOperator(
        task_id = 'task_id_1',
        python_callable = get_weather_data,
        op_args = [WEATHER_API, ACCSESS_KEY_ID, SECRET_ACCESS_KEY]
    )