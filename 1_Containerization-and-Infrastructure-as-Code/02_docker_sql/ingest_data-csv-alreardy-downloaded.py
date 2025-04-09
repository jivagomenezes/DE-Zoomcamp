import pandas as pd
from sqlalchemy import create_engine

df_iter = pd.read_csv('yellow_tripdata_2021-01.csv', iterator=True, chunksize=100000)

df = next(df_iter)
df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

engine = create_engine('postgresql://root:root@localhost:5433/ny_taxi')

# Create table
df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

# Insert first chunk
df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

# Insert remaining data
while True: 
    try:
       
        df = next(df_iter)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)    
        df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')

        print('inserted another chunk')
    except StopIteration:
        print('completed')
        break
