# -*- coding: utf-8 -*-
import os.path
import sys

try:
    import secret
except ImportError:
    sys.stderr.write(""">> You should create secret.py next to config.py to define the secret key:
# -*- coding: utf-8 -*-
SECRET_KEY = 'qwerty123456'
""")
    raise

LANGUAGES = ['fr', 'en', 'zh']
BABEL_DEFAULT_LOCALE = 'fr'
SECRET_KEY = secret.SECRET_KEY

# Bower configuration
BOWER_PATH = os.path.join(os.path.dirname(__file__),
                          'static/bower_components')

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
