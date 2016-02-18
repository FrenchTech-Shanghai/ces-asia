# -*- coding: utf-8 -*-
from os.path import abspath, join

from flask import Flask, render_template, request, g, abort
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


@app.before_request
def before():
    if request.view_args and 'lang' in request.view_args:
        if request.view_args['lang'] not in app.config['LANGUAGES']:
            return abort(404)
        g.current_lang = request.view_args['lang']
        request.view_args.pop('lang')
    else:
        g.current_lang = app.config['BABEL_DEFAULT_LOCALE']

@babel.localeselector
def get_locale():
    if 'current_lang' in g:
        return g.get('current_lang')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/<lang>/signup/')
@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/<lang>/')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
