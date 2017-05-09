# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify, session, request
from .logic import print_head
from .logic import get_date_json

sfpd = Blueprint('sfpd', __name__, url_prefix='/sfpd')


@sfpd.route('/')
@sfpd.route('/main/')
def main():
    print_head()
    return render_template('modules/sfpd/sfpd.html')

@sfpd.route('/first_json/')
def first_json():
    dict_ret = {
        'full_timeseries': get_date_json()
    }
    return jsonify(dict_ret)

@sfpd.route('/first/')
def first():
    return render_template('modules/sfpd/first.html')

