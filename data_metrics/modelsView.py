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


class EventCountView(ModelView):
    column_labels = {
        "day": u"日期",
        "project_id": u'项目ID',
        "event_id": u'事件',
        "counts": u'条数',
        "users": u'用户数',
        "avg_counts": u'人均条数'
    }
    column_display_pk = True
    can_delete = False
    can_edit = False
    can_create = False
    column_searchable_list = ['project_id', 'event_id']
    column_filters = ['day', 'project_id', 'event_id']
    # column_editable_list = ['name']
