from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
import pendulum
    
dag = DAG(
    dag_id="test_k8s",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["samples1"],
)

KubernetesPodOperator(
    name="hello-dry-run",
    image="debian",
    cmds=["bash", "-cx"],
    arguments=["echo", "10"],
    labels={"foo": "bar"},
    task_id="dry_run_demo",
    do_xcom_push=True,
)