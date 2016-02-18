# -*- coding: utf-8 -*-
from os.path import abspath, join

from flask import Flask, render_template, request, session
from flask.ext.babel import Babel
from flask.ext.assets import Environment, Bundle

import config


app = Flask(__name__)
app.config.from_object(config)
assets = Environment(app)
babel = Babel(app)

assets.config['libsass_includes'] = [app.config['BOWER_PATH'], ]

style = Bundle('css/style.scss',
               filters='libsass',
               output='css/style.css',
               depends='css/*/*.scss')
assets.register('localstyle', style)

@babel.localeselector
def get_locale():
    if 'lang' in session and \
        session['lang'] in app.config['LANGUAGES']:
        return session['lang']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/signup/<lang>/')
@app.route('/signup/')
def signup(lang=None):
    return render_template('signup.html')

@app.route('/<lang>/')
@app.route('/')
def index(lang=None):
    if lang is not None:
        if lang not in app.config['LANGUAGES']:
            lang = None
        session['lang'] = lang

    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
