FROM python:3.9.1


RUN pip install pandas sqlalchemy psycopg2 requests

WORKDIR /app
COPY ingest_data.py ingest_data.py 

ENTRYPOINT [ "python3", "ingest_data.py" ]