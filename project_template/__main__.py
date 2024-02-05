import logging
from .config import NAME
from .scripts import download_data_gbq, download_data_redshift


log = logging.getLogger(__name__)


log.info(f'Start running project name: {NAME}')
download_data_gbq()
download_data_redshift()
log.info('All done.')
