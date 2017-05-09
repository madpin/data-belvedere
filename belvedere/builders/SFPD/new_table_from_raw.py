import os
import pandas as pd
from sqlalchemy import create_engine

from sqlalchemy import Table, Column, MetaData
from sqlalchemy import Integer, String, Enum
from sqlalchemy import DateTime, Date, Float, Text, Boolean, Numeric

from ..utils import APP_DATASOURCES


engine = create_engine('sqlite:///' +
                       os.path.join(APP_DATASOURCES, 'SFPD.db'))

df = pd.read_sql_query("""
SELECT
    DATE("Date") as "Date",
    count( DISTINCT IncidntNum ) AS incidents
FROM
    raw_data
GROUP BY
    DATE("Date");
""", engine)




DTYPE = {
    'date': Date(),
    'incidents': Numeric(),
}

df.to_sql(
    name='tb_date',
    con=engine,
    schema='SFPD',
    if_exists='replace',
    dtype=DTYPE
)