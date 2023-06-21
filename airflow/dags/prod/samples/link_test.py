from airflow import models
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
 
default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2020, 2, 9),
        'retries': 1,
        'retry_delay': timedelta(minutes=5)}
 
with models.DAG(
        dag_id='echo_test', description='echo_test',
        schedule_interval=None,
        max_active_runs=5,
        concurrency=10,
        default_args=default_args) as dag:
 
 
    command_1 = BashOperator(
            task_id='ls',
            bash_command='ls -al',
            dag=dag)
 
    command_2 = BashOperator(
            task_id='pwd',
            bash_command="pwd",
            dag=dag)
 
    command_3 = BashOperator(
            task_id='realpath',
            bash_command='realpath .',
            dag=dag)
 
    command_1 >> command_2 >> command_3
    # 이것은 위의 task를 이어주는 줄입니다.
