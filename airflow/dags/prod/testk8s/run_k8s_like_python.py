from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
import pendulum
    
dag = DAG(
    dag_id="test_k8s_django",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["samples1"],
)

KubernetesPodOperator(
    dag=dag,
    name="hello-django-run",
    image="django",
    cmds=["python3", "manage.py" "version"],
    task_id="dry_run_demo_django",
    do_xcom_push=True,
)