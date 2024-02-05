from importlib import resources
from google.cloud import bigquery

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


class GBQIterator:
    '''
        Execute a BigQuery SQL query and save the result to a JSONL file with Gzip compression.

        :param query: A string that represents the SQL query to be executed.
    '''
    def __init__(self, query:str, itersize:int=10_000):
        self.client = bigquery.Client()
        self.query = query
        self.itersize = itersize

    def __iter__(self):
        query_job = self.client.query(self.query)
        result = query_job.result()
        destination_table = query_job.destination

        for i in range(0, result.total_rows, self.itersize):
            rows_iter = self.client.list_rows(destination_table, max_results=self.itersize, start_index=i)
            for row in rows_iter:
                yield row
