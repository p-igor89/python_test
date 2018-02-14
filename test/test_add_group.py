# -*- coding: utf-8 -*-
from model.group import Group


def test_app_group(app):
    app.session.login("secret", "admin")
    app.group.create(Group("Example", "Address", "Notes"))
    app.session.logout()


def test_app_empty_group(app):
    app.session.login("secret", "admin")
    app.group.create(Group("", "", ""))
    app.session.logout()
