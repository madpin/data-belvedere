# -*- coding: utf-8 -*-
"""
    Utils has nothing to do with models and views.
"""

import string
import random
import os

from datetime import datetime


# Instance folder path, make it independent. 
INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')


# __file__ refers to the file settings.py
# refers to application_top
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_DATASOURCES = os.path.join(APP_ROOT, 'datasources')
APP_STATIC = os.path.join(APP_ROOT, 'static')

def id_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
    except Exception as e:
        raise e

def to_highcharts_utc_date(date_):
    import time
    import datetime
    # date_.to_datetime()
    date = time.mktime(date_.timetuple())*1000
    return date
