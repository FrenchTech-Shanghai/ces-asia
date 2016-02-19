# -*- coding: utf-8 -*-
from os.path import abspath, join

from flask import Flask, render_template, request, g, abort, flash
from flask.ext.babel import Babel, lazy_gettext
from flask.ext.assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_wtf import Form
from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

import config


app = Flask(__name__)
app.config.from_object(config)
assets = Environment(app)
babel = Babel(app)
db = SQLAlchemy(app)

assets.config['libsass_includes'] = [app.config['BOWER_PATH'], ]

style = Bundle('css/style.scss',
               filters='libsass, cssmin',
               output='css/style.css',
               depends='css/*/*.scss')
assets.register('localstyle', style)

purecss = Bundle('bower_components/pure/base-min.css',
                 'bower_components/pure/buttons-core-min.css',
                 'bower_components/pure/buttons-min.css',
                 'bower_components/pure/forms-min.css',
                 filters='cssmin',
                 output='css/pure.css')
assets.register('purecss', purecss)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(254))
    contact = db.Column(db.String(254))
    email = db.Column(db.String(254), unique=True)

    def __init__(self, name, contact, email):
        self.name = name
        self.contact = contact
        self.email = email

    def __repr__(self):
        return '<Company {}>'.format(self.company)


class SignupForm(Form):
    name = StringField(lazy_gettext(u'Company name'), validators=[DataRequired()])
    contact = StringField(lazy_gettext(u'Contact name'), validators=[DataRequired()])
    email = EmailField(lazy_gettext(u'Contact email'), validators=[DataRequired(), Email()])


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


@app.route('/<lang>/signup/', methods=['GET', 'POST'])
@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit() == False:
            flash(lazy_gettext(u'All fields are required'))
            return render_template('signup.html', form=form)
        else:
            startup = Company(**form.data)
            db.session.add(startup)
            try:
                db.session.commit()
            except IntegrityError:
                flash(lazy_gettext(u'This company email is already signed up'))
                return render_template('signup.html', form=form)
            return render_template('signup.html', form=form)
    elif request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route('/<lang>/')
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
