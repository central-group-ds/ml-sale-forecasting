import time
from typing import Iterator
from importlib import resources
import psycopg2
import pandas as pd
from psycopg2.extras import RealDictCursor, RealDictRow
from ..config import REDSHIFT_CONFIG


'''
    SQL files are named as 'prefix_name.sql'
    - SQL scripts executed "automatically" have 'a' in prefix.
    - SQL scripts executed "manually" have 'm' in prefix.
'''
QUERIES_A, QUERIES_M = {}, {}
for file in resources.files(__package__).iterdir():
    if file.name.endswith('.sql'):
        prefix, name = file.name.removesuffix('.sql').split('_', 1)
        if 'a' in prefix:
            QUERIES_A[name] = file.read_text()
        if 'm' in prefix:
            QUERIES_M[name] = file.read_text()


class RedshiftIterator:
    def __init__(self, name:str, query:str):
        self.name = f'{name}-{int(time.time())}'.replace('_', '-')
        self.query = query

    def __iter__(self) -> Iterator[RealDictRow]:
        with psycopg2.connect(**REDSHIFT_CONFIG) as conn:
            with conn.cursor(self.name, RealDictCursor) as cur:
                cur.itersize = 50_000
                cur.execute(self.query)
                for row in cur:
                    yield row
        conn.close()


def query_redshift(query):
    conn = psycopg2.connect(**REDSHIFT_CONFIG)
    cursor = conn.cursor()
    df = pd.read_sql(query, conn)
    cursor.close()
    conn.close()

    return df
