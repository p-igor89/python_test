from model.group import Group


def test_modify_name_group(app):
    app.group.modify_first_group(Group(name='New Group'))


def test_modify_header_group(app):
    app.group.modify_first_group(Group(header='New header'))
