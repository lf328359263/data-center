# -*- coding: UTF-8 -*-
from flask import Flask
import data_metrics.views
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config_filename):
    app = Flask(__name__)
    # app.config.from_pyfile(config_filename)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask-app'

    # from data_metrics.database import db_session

    # @app.teardown_appcontext
    # def shutdown_session(exception=None):
    #     db_session.remove()
    # from data_metrics.model import db
    db.init_app(app)

    # from data_metrics.views.admin import admin
    # from data_metrics.views.frontend import frontend
    # app.register_blueprint(admin)
    # app.register_blueprint(frontend)

    # from data_metrics.views import base
    # app.register_blueprint(base)

    app.config['FLASK_ADMIN_SWATCH'] = 'Paper'
    admin = Admin(app, name=u'数据管理系统', template_mode='bootstrap3')

    from .models import Users
    admin.add_view(ModelView(Users, db.session, category=u'系统管理', name=u'用户列表'))

    return app


