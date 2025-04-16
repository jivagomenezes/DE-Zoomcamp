#!/bin/bash

# Configuração do JDK
export JAVA_HOME=/home/jivagomenezes/00-dev/01-Projects/01-Data-Engineer/01-Active/02-zoomcamp-datatalks/05_Batch-Processing-Spark/jdk-11.0.2
export PATH=$JAVA_HOME/bin:$PATH

# Ativar ambiente virtual do Python
. /home/jivagomenezes/00-dev/01-Projects/01-Data-Engineer/01-Active/02-zoomcamp-datatalks/05_Batch-Processing-Spark/spark_env/bin/activate

# Verificar instalações
echo "==== Verificação do Java ===="
java -version
echo

echo "==== Verificação do PySpark ===="
python -c "import pyspark; print('PySpark versão:', pyspark.__version__)"
echo

echo "Ambiente configurado com sucesso!"
