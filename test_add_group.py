# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_app_group(app):
    app.open_home_page()
    app.login("secret", "admin")
    app.create_group(Group("Example", "Address", "Notes"))
    app.logout()


def test_app_empty_group(app):
    app.open_home_page()
    app.login("secret", "admin")
    app.create_group(Group("", "", ""))
    app.logout()
