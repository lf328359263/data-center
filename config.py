# -*- coding: UTF-8 -*-
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask-app'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_BINDS = {
    'ga': 'mysql+pymysql://root:123456@127.0.0.1:3306/ga'
}

DEBUG = True
SECRET_KEY = 'TPmi4aLWRbyVq8zu9v82dWYW1'
BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

# UPLOAD_FOLDER = 'F:\\uploadFile'
# MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Flask-Security config
SECURITY_URL_PREFIX = "/admin"
SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = "/login/"
SECURITY_LOGOUT_URL = "/logout/"
SECURITY_REGISTER_URL = "/register/"

SECURITY_POST_LOGIN_VIEW = "/admin/"
SECURITY_POST_LOGOUT_VIEW = "/admin/"
SECURITY_POST_REGISTER_VIEW = "/admin/"

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
