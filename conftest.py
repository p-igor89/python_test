import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.isValid():
            fixture = Application()
    fixture.session.ensureLogin(userName="admin", password="secret")
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensureLogout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
