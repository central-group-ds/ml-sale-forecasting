# %%
import logging
from IPython.display import display
import pandas as pd

from project_template.config import FILEPATHS
from project_template.config import DATE_RANGE, LIST_DEPT
from project_template.redshift import QUERIES_M, query_redshift
from project_template.scripts.download_data import download_data_redshift


log = logging.getLogger(__name__)

# %% [markdown]
# ### Query data from AWS Redshift with psycopg2 package

# %%
download_data_redshift()

# %%
df = pd.read_json(FILEPATHS['test_redshift'], lines=True)
df.head(3)

# %% [markdown]
# ### Query data from AWS Redshift as dataframe

# %%
QUERIES_M

# %%
print(QUERIES_M['test_redshift'])

# %%
parameters = {
    'DATE_RANGE': DATE_RANGE,
    'WHERE_DEPARTMENT': ' AND department in (' + ', '.join(f'"{w}"' for w in LIST_DEPT) + ') ' if len(LIST_DEPT) > 0 else ' '
}
print(QUERIES_M['test_redshift'].format(**parameters))

# %%
df2 = query_redshift(QUERIES_M['test_redshift'].format(**parameters))
df2.head(3)

# %% [markdown]
#
