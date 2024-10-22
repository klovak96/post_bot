from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Функция для запуска вашего Jupyter Notebook
def run_bot_notebook():
    subprocess.run(["jupyter", "nbconvert", "--to", "script", "/path/to/your/notebook/pbot.ipynb"])
    subprocess.run(["python", "/path/to/your/notebook/pbot.py"])

# Определение DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 10, 22),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'telegram_bot_dag',
    default_args=default_args,
    description='DAG for running Telegram bot',
    schedule_interval = '* * * * *',
    #schedule_interval='0 9,11,13,15,17,19,21, * * *',
)

run_bot = PythonOperator(
    task_id='run_bot_notebook',
    python_callable=run_bot_notebook,
    dag=dag,
)