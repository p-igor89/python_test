# -*- coding: utf-8 -*-
from model.group import Group


def test_app_group(app):
    oldGroup = app.group.get_Group_list()
    app.group.create(Group("Example", "Address", "Notes"))
    newGroup = app.group.get_Group_list()
    assert len(oldGroup) + 1 == len(newGroup)


def test_app_empty_group(app):
    oldGroup = app.group.get_Group_list()
    app.group.create(Group("", "", ""))
    newGroup = app.group.get_Group_list()
    assert len(oldGroup) + 1 == len(newGroup)
