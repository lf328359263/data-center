# -*- coding: UTF-8 -*-
from flask import Flask
from flask_admin import Admin, AdminIndexView
from flask_sqlalchemy import SQLAlchemy
from flask_babelex import Babel
from data_metrics.modelsView import UserView, EventCountView
import config


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    babel = Babel(app)

    db.init_app(app)

    app.config['FLASK_ADMIN_SWATCH'] = 'Paper'
    admin = Admin(app,
                  name=u'数据质量',
                  template_mode='bootstrap3',
                  index_view=AdminIndexView(
                      url='/'
                  )
                  )

    from .models import Users, EventCount
    admin.add_view(UserView(Users, db.session, category=u'系统管理', name=u'用户列表'))
    admin.add_view(EventCountView(EventCount, db.session, category=u'项目统计', name=u'事件统计'))

    from auth.models import user_datastore, Role, User
    from auth.modelsView import SecurityModelView
    from flask_security import Security
    security = Security(app, user_datastore)

    admin.add_view(SecurityModelView(Role, db.session))
    admin.add_view(SecurityModelView(User, db.session))

    # admin.add_sub_category(name="Links", parent_name=u'系统管理')
    # admin.add_link(MenuLink(name='Home Page', url='/', category='Links'))

    return app


