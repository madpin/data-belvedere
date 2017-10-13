# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify, session, request
from .logic import print_head
from .logic import get_incidents_json
from .logic import get_all_data

sfpd = Blueprint('sfpd', __name__, url_prefix='/sfpd')


@sfpd.route('/')
@sfpd.route('/main/')
def main():
    # print_head()
    return render_template('modules/sfpd/sfpd.html')

@sfpd.route('/first_json/')
def first_json():
    dict_ret = {
        'full_timeseries': get_incidents_json()
    }
    return jsonify(dict_ret)

@sfpd.route('/first/')
def first():
    return render_template('modules/sfpd/first.html')


@sfpd.route('/all_data_json/', methods=['POST'])
def all_data_json():
    parameters = {}
    parameters['draw'] = request.form.get('draw', default = 1, type = int)
    parameters['start'] = request.form.get('start', default = 0, type = int)
    parameters['length'] = request.form.get('length', default = 50, type = int)
    parameters['order_column'] = request.form.get('order[0][column]', default = 0, type = int)+1
    parameters['order_dir'] = request.form.get('order[0][dir]', default = 'asc', type = str)

    return jsonify(get_all_data(parameters))


@sfpd.route('/all_data/')
def all_data():
    return render_template('modules/sfpd/all_data.html')

