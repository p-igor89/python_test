# -*- coding: utf-8 -*-
from model.group import Group


def test_app_group(app):
    app.group.create(Group("Example", "Address", "Notes"))


def test_app_empty_group(app):
    app.group.create(Group("", "", ""))
