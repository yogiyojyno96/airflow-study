import pendulum

from airflow import DAG
from airflow.decorators import task

with DAG(
    dag_id="example_python_operator_print",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["samples"],
) as dag:

    @task()
    def print_test():
        """Print Numpy array."""
        print("Test")
        return "Test"

    print_test()