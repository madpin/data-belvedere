# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify, session, request


blank = Blueprint('blank', __name__, url_prefix='/blank')


@blank.route('/')
@blank.route('/main/')
def main():
    return render_template('modules/blank/blank.html')
