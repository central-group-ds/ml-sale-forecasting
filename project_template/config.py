import os
import sys
import logging
from pathlib import Path


#Configure logging.
sys.excepthook = lambda *args: logging.exception('', exc_info=args)
logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
    level=logging.INFO,
    force=True
)


#Configure environment.
ENVIRONMENT = os.getenv('ENVIRONMENT', 'staging')
logging.info(f'ENVIRONMENT is set to {ENVIRONMENT}')
assert ENVIRONMENT in ('production', 'staging'), 'Unknown environment.'


#Model name and version.
NAME = 'project_template'
VERSION = 1


#Database configs.
REDSHIFT_CONFIG = {
     'host': os.getenv('REDSHIFT_HOST', 'redshift-cluster-1.the1data.studio'),
     'port': os.getenv('REDSHIFT_PORT', '5439'),
     'user': os.getenv('REDSHIFT_USER', '<user>'),              # config here or in environment variables
     'password': os.getenv('REDSHIFT_PASS', '<password>'),      # config here or in environment variables
     'dbname': 'the1'
}
SERVICE_ACCOUNT_JSON = 'gcp_service_account.json'


#Query configs.
DATE_RANGE = ('2022-01-01', '2022-01-31')
LIST_DEPT = ['001 - BEAUTY', '003 - WOMEN']


#File configs.
TEMP_DIR = Path('temp')
BUNDLE_LIST = []
FILENAMES = {
    'test_bigquery': 'test_bigquery.jsonl.gz',
    'test_bigquery_csv': 'test_bigquery.csv',
    'test_redshift': 'test_redshift.jsonl.gz',
    'test_redshift_csv': 'test_redshift.csv',
}
FILEPATHS = {k: os.path.join(TEMP_DIR, v) for k, v in FILENAMES.items()}
