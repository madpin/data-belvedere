# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify, session, request


profile = Blueprint('profile', __name__, url_prefix='/profile')


@profile.route('/')
@profile.route('/main/')
def main():
    return render_template('modules/profile/profile.html')
