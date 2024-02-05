# %%
import logging
from IPython.display import display
import pandas as pd
import pandas_gbq

from project_template.config import FILEPATHS
from project_template.config import DATE_RANGE, LIST_DEPT
from project_template.bigquery import QUERIES_M
from project_template.scripts.download_data import download_data_gbq


log = logging.getLogger(__name__)

# %% [markdown]
# ### Query data from Google BigQuery with bigquery package

# %%
download_data_gbq()

# %%
df = pd.read_json(FILEPATHS['test_bigquery'], lines=True)
df.head(3)

# %% [markdown]
# ### Query data from Google BigQuery with pandas_gbq

# %%
QUERIES_M

# %%
print(QUERIES_M['test_bigquery'])

# %%
# substitute sql patameters
parameters = {
    'DATE_RANGE': DATE_RANGE,
    'WHERE_DEPARTMENT': ' AND department in (' + ', '.join(f'"{w}"' for w in LIST_DEPT) + ') ' if len(LIST_DEPT) > 0 else ' '
}
print(QUERIES_M['test_bigquery'].format(**parameters))

# %%
df2 = pandas_gbq.read_gbq(QUERIES_M['test_bigquery'].format(**parameters))
df2.head(3)
