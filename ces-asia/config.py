# -*- coding: utf-8 -*-
import os.path

LANGUAGES = ['fr', 'en', 'zh_CN']
BABEL_DEFAULT_LOCALE = 'fr'
SECRET_KEY = 'test'

# Bower configuration
BOWER_PATH = os.path.join(os.path.dirname(__file__),
                          'static/bower_components')
