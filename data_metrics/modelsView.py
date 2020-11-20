# -*- coding: UTF-8 -*-

from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    column_labels = {
        "id": "ID",
        "name": u'名称',
        "email": u'邮箱'
    }
    can_delete = False
    column_searchable_list = ['name', 'email']
    column_filters = ['name']
    column_editable_list = ['name']
