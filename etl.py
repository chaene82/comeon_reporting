import requests
import pandas as pd
import datetime as dt
import sqlite3
from sqlalchemy import create_engine
engine = create_engine('sqlite:///test.db', echo=True)

base_url = "https://beaconcha.in/api/v1/"

node_hash_list = ['0xb8ccfffc61240c05a77a4f5619dcec2e99942a7d2a3b441e4ce789bb95d1c88df1ff702dbc552694661fbb888cee7ae9', 
                '0xa685b19738ac8d7ee301f434f77fdbca50f7a2b8d287f4ab6f75cae251aa821576262b79ae9d58d9b458ba748968dfda',
                '0xb451fd4d4f59d519809dbdaf62cddea93442aa2a5fc490f96e1ba1622e6437a75591c5fd026ebb8152fa82bd356b7686']


def getStatusETHNode(base_url, node_hash):
    response = requests.get(base_url + 'validator/' + node_hash)
    return response.json()['status']

def getStatsETHNode(base_url, node_hash):
    response = requests.get(base_url + 'validator/' + node_hash + '/performance')
    df = pd.DataFrame.from_dict(response.json()['data'])
    df['node'] = node_hash
    df['node_short'] = node_hash[:5]   
    df['timestamp'] = dt.datetime.now()
    return df

for node_hash in node_hash_list:
    print(getStatusETHNode(base_url, node_hash))
    df = getStatsETHNode(base_url, node_hash)
    df.to_sql(name='eth_node_stats',if_exists='append', con=engine, )



