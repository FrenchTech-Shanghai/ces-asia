# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session
from flask.ext.babel import Babel
from flask.ext.assets import Environment, Bundle


LANGUAGES = ['en', 'zh', 'fr']
SECRET_KEY = 'test'

app = Flask(__name__)
app.config.from_object(__name__)
assets = Environment(app)
babel = Babel(app)

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


@app.route('/<lang>/')
@app.route('/')
def index(lang=None):
    return render_template('signup.html')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
