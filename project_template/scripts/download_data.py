import os
import logging
import gzip
import json
import pandas_gbq
import google.auth
from .. import redshift
from .. import bigquery
from ..config import FILEPATHS, NAME, SERVICE_ACCOUNT_JSON
from ..config import DATE_RANGE, LIST_DEPT


log = logging.getLogger(__name__)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SERVICE_ACCOUNT_JSON

# Create credentials with Drive & BigQuery API scopes and add to pandas_gbq
credentials, project = google.auth.default(
    scopes=[
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/bigquery',
    ]
)
pandas_gbq.context.credentials = credentials
pandas_gbq.context.project = project


# Substitute parameters
parameters = {
    'DATE_RANGE': DATE_RANGE,
    'WHERE_DEPARTMENT': ' AND department in (' + ', '.join(f'"{w}"' for w in LIST_DEPT) + ') ' if len(LIST_DEPT) > 0 else ' '
}


def download_data_redshift():
    # Query data in Redshift for all automated sql scripts
    QUERIES = redshift.QUERIES_A
    log.info('Downloading data from Redshift...')
    for name, query in QUERIES.items():
        log.info(f'Downloading {name}...')

        if FILEPATHS[name].endswith('.jsonl.gz'):
            with gzip.open(FILEPATHS[name], 'wt', compresslevel=5) as f:
                for row in redshift.RedshiftIterator(NAME, query.format(**parameters)):
                    f.write(json.dumps(row, default=str) + '\n')
        elif FILEPATHS[name].endswith('.csv'):
            df = redshift.query_redshift(query.format(**parameters))
            df.to_csv(FILEPATHS[name], index=False)
            del df
    log.info('Downloaded all files successfully.')

def download_data_gbq():
    # Query data in GBQ for all automated sql scripts
    QUERIES = bigquery.QUERIES_A
    log.info('Downloading data from Google BigQuery...')
    for name, query in QUERIES.items():
        log.info(f'Downloading {name}...')

        if FILEPATHS[name].endswith('.jsonl.gz'):
            with gzip.open(FILEPATHS[name], 'wt', compresslevel=5) as f:
                for row in bigquery.GBQIterator(query=query.format(**parameters)):
                    f.write(json.dumps(dict(row), default=str) + '\n')
        elif FILEPATHS[name].endswith('.csv'):
            df = pandas_gbq.read_gbq(query.format(**parameters))
            df.to_csv(FILEPATHS[name], index=False)
            del df
    log.info('Downloaded all files successfully.')
