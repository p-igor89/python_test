# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_app_group(app):
    app.session.login("secret", "admin")
    app.group.create(Group("Example", "Address", "Notes"))
    app.session.logout()


def test_app_empty_group(app):
    app.session.login("secret", "admin")
    app.group.create(Group("", "", ""))
    app.session.logout()
