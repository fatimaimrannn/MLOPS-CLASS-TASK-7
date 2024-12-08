from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Dummy function to simulate fetching raw data
def fetch_weather_data():
    print("Fetching weather data... []")
    # Simulate a successful operation
    print(" weather data fetched successfully.")

# Dummy function to simulate preprocessing data
def preprocess_weather_data():
    print("Preprocessing weather data... []")
    # Simulate a successful operation
    print(" weather data preprocessed successfully.")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'start_date': datetime(2023, 11, 1),
}

# Define the DAG
with DAG(
    'weather_data_pipeline2',
    default_args=default_args,
    description='A pipeline for testing Airflow',
    schedule_interval=None,  # Change to '@daily' or your preferred schedule
    catchup=False,
) as dag:

    # Task 1: Fetch raw data
    fetch_data_task = PythonOperator(
        task_id='fetch_raw_weather_data',
        python_callable=fetch_weather_data,
    )

    # Task 2: Preprocess the data
    preprocess_data_task = PythonOperator(
        task_id='preprocess_weather_data',
        python_callable=preprocess_weather_data,
    )

    # Define task dependencies
    fetch_data_task >> preprocess_data_task
