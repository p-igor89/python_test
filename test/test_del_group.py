from model.group import Group


def test_del_first_group(app):
    oldGroup = app.group.get_Group_list()
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    app.group.del_first_group()
    newGroup = app.group.get_Group_list()
    assert len(oldGroup) - 1 == len(newGroup)
