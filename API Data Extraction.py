import requests

api = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(api)
if response:
    print('Data retrieved')
else:
    print('Data not found')

data = response.json()

import psycopg2
import pandas as pd
from sqlalchemy import create_engine
import json

hostname = 'localhost'
database = 'demo'
username = 'postgres'
pwd = '250857'
port_id = 5432
conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    cur = conn.cursor()
    table_name = 'q8_csv'

    def etl_process(json_data,postgreuri,table_name):

        df = pd.DataFrame(json_data)

        engine = create_engine(postgreuri)

        df.to_sql(table_name,engine,if_exists='replace',index=False)

    postgreuri = 'postgresql://postgres:250857@localhost:5432/demo'
    etl_process(data,postgreuri,table_name)

except Exception as error:
    print("Error:", error)

finally:

    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()