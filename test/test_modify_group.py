from model.group import Group


def test_modify_name_group(app):
    app.session.login("secret", "admin")
    app.group.modify_first_group(Group(name='New Group'))
    app.session.logout()


def test_modify_header_group(app):
    app.session.login("secret", "admin")
    app.group.modify_first_group(Group(header='New header'))
    app.session.logout()
