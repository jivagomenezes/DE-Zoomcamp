"""
Script para modificar o executor do Airflow para LocalExecutor.
Este script cria um arquivo de configuração temporário e se conecta ao pod do scheduler
para aplicar as mudanças.
"""
import os
import subprocess
import time

# Nome do pod do scheduler no namespace airflow
SCHEDULER_POD = "airflow-scheduler-755f9577f8-8qmv7"
NAMESPACE = "airflow"

# Conteúdo da alteração de configuração
CONFIG_CONTENT = """
[core]
executor = LocalExecutor

[celery]
executor = LocalExecutor

[scheduler]
executor = LocalExecutor
"""

def main():
    print("Iniciando processo de alteração do executor para LocalExecutor...")
    
    # Criando um arquivo temporário com as configurações
    config_file = "airflow_local_exec.cfg"
    with open(config_file, "w") as f:
        f.write(CONFIG_CONTENT)
    
    print(f"Arquivo de configuração criado: {config_file}")
    
    # Copiando o arquivo para o pod
    print(f"Copiando arquivo para o pod {SCHEDULER_POD}...")
    subprocess.run([
        "kubectl", "cp", 
        config_file, 
        f"{NAMESPACE}/{SCHEDULER_POD}:/tmp/airflow_local_exec.cfg"
    ])
    
    # Aplicando as mudanças no scheduler
    print("Aplicando configurações no arquivo airflow.cfg...")
    subprocess.run([
        "kubectl", "exec", "-it", 
        f"{SCHEDULER_POD}", 
        "-n", NAMESPACE, 
        "--", "bash", "-c",
        "cat /tmp/airflow_local_exec.cfg >> /opt/airflow/airflow.cfg"
    ])
    
    # Verificando se a alteração foi aplicada
    print("Verificando configuração atual...")
    subprocess.run([
        "kubectl", "exec", "-it", 
        f"{SCHEDULER_POD}", 
        "-n", NAMESPACE, 
        "--", "grep", "executor", "/opt/airflow/airflow.cfg"
    ])
    
    # Reiniciando os pods necessários
    print("Reiniciando o pod do scheduler...")
    subprocess.run([
        "kubectl", "delete", "pod", 
        f"{SCHEDULER_POD}", 
        "-n", NAMESPACE
    ])
    
    print("Aguardando reinicialização dos pods...")
    time.sleep(10)
    
    # Listando pods após reinício
    print("Listando pods:")
    subprocess.run([
        "kubectl", "get", "pods", 
        "-n", NAMESPACE
    ])
    
    print("\nProcesso concluído! Verifique se o executor foi alterado para LocalExecutor.")
    print("Tente executar novamente o DAG hello_world_dag após a reinicialização completa dos pods.")

if __name__ == "__main__":
    main()
