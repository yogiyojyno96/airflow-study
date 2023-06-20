from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from kubernetes.client import models as k8s
import pendulum
    
dag = DAG(
    dag_id="test_k8s_1",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["samples1"],
)

KubernetesPodOperator(
    dag=dag,
    namespace="example-namespace",
    image="your-image-name:tag",
    image_pull_secrets=[k8s.V1LocalObjectReference("testquay")],
    cmds=["bash", "-cx"],
    arguments=["echo", "10", "echo pwd"],
    labels={"foo": "bar"},
    name="airflow-private-image-pod",
    is_delete_operator_pod=True,
    in_cluster=True,
    task_id="task-two",
)
