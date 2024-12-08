from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import os
import subprocess

# Function to fetch raw data
def fetch_weather_data():
    try:
        # Define the path to the fetch_weather.py script
        script_path = os.path.join(os.path.dirname(__file__), "../../fetch_weather.py")
        script_path = os.path.abspath(script_path)

        # Run the fetch_weather.py script
        subprocess.run(["python", script_path], check=True)
        print("Successfully fetched raw data and saved to raw_data.csv.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while fetching weather data: {e}")
        raise
    except FileNotFoundError as e:
        print(f"Script not found: {e}")
        raise

# Function to preprocess data
def preprocess_weather_data():
    try:
        # Define the path to the preprocess.py script
        script_path = os.path.join(os.path.dirname(__file__), "../../fetch_weather.py")
        script_path = os.path.abspath(script_path)

        # Run the preprocess.py script
        subprocess.run(["python", script_path], check=True)
        print("Successfully preprocessed data and saved to processed_data.csv.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while preprocessing weather data: {e}")
        raise
    except FileNotFoundError as e:
        print(f"Script not found: {e}")
        raise

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
    'weather_data_pipeline',
    default_args=default_args,
    description='A pipeline for fetching and preprocessing weather data',
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
