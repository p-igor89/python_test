from model.group import Group


def test_modify_name_group(app):
    oldGroup = app.group.get_Group_list()
    app.group.modify_first_group(Group(name='New Group'))
    newGroup = app.group.get_Group_list()
    assert len(oldGroup) == len(newGroup)


def test_modify_header_group(app):
    oldGroup = app.group.get_Group_list()
    app.group.modify_first_group(Group(header='New header'))
    newGroup = app.group.get_Group_list()
    assert len(oldGroup) == len(newGroup)
