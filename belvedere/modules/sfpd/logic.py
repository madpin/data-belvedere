import pandas as pd
from sqlalchemy import create_engine
import os
from ...utils import APP_DATASOURCES
from ...utils import to_highcharts_utc_date


file_path = os.path.join(APP_DATASOURCES, 'SFPD.db')


def print_head():

    engine = create_engine('sqlite:///' + file_path)
    df = pd.read_sql_query("""
    SELECT
        *
    FROM
        raw_data
    """, engine)

    print(df.head())
    # return
    return 1


def get_date_json():
    engine = create_engine('sqlite:///' + file_path)
    
    df = pd.read_sql_query("""
    SELECT date_, incidents FROM pd_date;
    """, engine)

    df['date_'] = pd.to_datetime(df['date_'], format='%Y-%m-%d', errors='ignore')
    df['date_'] = df['date_'].apply(to_highcharts_utc_date)
    dict_ret = {
        'name': 'first of many',
        'values': df.values.tolist(),
        'columns': df.columns.tolist(),
    }
    # return
    return dict_ret