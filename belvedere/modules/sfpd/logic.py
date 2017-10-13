import pandas as pd
from sqlalchemy import create_engine
import os
from ...utils import APP_DATASOURCES
from ...utils import to_highcharts_utc_date


file_path = os.path.join(APP_DATASOURCES, 'SFPD.db')


def print_head():
    print("File Path: " + file_path)

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


def get_incidents_json():
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


def get_all_data(parameters):
    obj_to_return = {}

    engine = create_engine('sqlite:///' + file_path)
    conn = engine.connect()

    recordsTotal_query = "SELECT COUNT(0) FROM raw_data"
    recordsTotal = conn.execute(recordsTotal_query).fetchone()


    all_data_query = """
    select
        id,
        Category,
        Descript,
        "Date",
        "Time",
        Resolution
    from
        raw_data 
    order by {order_column} {order_dir}    
    limit {start}, {length}
    """.format(
        start=parameters['start'],
        length=parameters['length'],
        order_column=parameters['order_column'],
        order_dir=parameters['order_dir'],
    )

    all_data_res = conn.execute(all_data_query)

    data = ([([r2[1] for r2 in row.items()]) for row in all_data_res])

    obj_to_return['draw'] = parameters['draw']
    obj_to_return['recordsTotal'] = recordsTotal[0]
    obj_to_return['recordsFiltered'] = recordsTotal[0]
    obj_to_return['data'] = data

    return obj_to_return