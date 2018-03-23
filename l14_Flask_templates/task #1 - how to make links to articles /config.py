# -*- coding: utf-8 -*-

__author__ = 'BorisRubin'


DEBUG = True
SECRET_KEY = 'BorisRubinSecretKey'

# Database settings:
SQLALCHEMY_DATABASE_URI = 'sqlite:///myblog.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False

