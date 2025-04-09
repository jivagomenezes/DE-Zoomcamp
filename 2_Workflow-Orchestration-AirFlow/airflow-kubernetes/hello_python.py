from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello_world_function():
    print("Hello World!")
    return "Hello World!"

dag = DAG(
    'hello_world_dag_python',  # Um nome diferente para não conflitar com o DAG existente
    description='Un simple DAG que imprime Hello World usando PythonOperator',
    schedule_interval=None,
    start_date=datetime(2025, 1, 6),
    catchup=False
)

hello_world_task = PythonOperator(
    task_id='hello_world_task',
    python_callable=hello_world_function,
    # Configuração específica para o KubernetesExecutor para garantir recursos adequados
    executor_config={
        "KubernetesExecutor": {
            "request_memory": "128Mi",
            "request_cpu": "100m",
            "limit_memory": "256Mi",
            "limit_cpu": "200m"
        }
    },
    dag=dag
)
