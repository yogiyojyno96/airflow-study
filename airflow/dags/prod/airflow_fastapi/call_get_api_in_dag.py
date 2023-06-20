from datetime import datetime
from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
import json


dag = DAG(
    dag_id="example_simple_http_operator_print_2",
    default_args={"retries": 1},
    tags=["simple http operator"],
    start_date=datetime(2021, 1, 1),
    catchup=False,
)

dag.doc_md = __doc__

# task_post_op, task_get_op and task_put_op are examples of tasks created by instantiating operators
# [START howto_operator_http_task_post_op]
task_post_op = SimpleHttpOperator(
    task_id="post_op",
    method="POST",
    endpoint="http://127.0.0.1:8000/items",
    data=json.dumps({"priority": 5}),
    headers={"Content-Type": "application/json"},
    dag=dag,
)

# [END howto_operator_http_task_post_op_formenc]
# [START howto_operator_http_task_get_op]
task_get_op = SimpleHttpOperator(
    task_id="get_op",
    endpoint="http://127.0.0.1:8000/items",
    data={"param1": "value1", "param2": "value2"},
    headers={},
    dag=dag,
)


task_post_op >> task_get_op