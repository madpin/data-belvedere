# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify, session, request


main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
@main.route('/index.html')
def main_func():
    return render_template('modules/profile/profile.html')
