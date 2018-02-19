from model.group import Group
from random import randrange


def test_del_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    oldGroup = app.group.get_Group_list()
    index = randrange(len(oldGroup))
    app.group.del_group_by_index(index)
    newGroup = app.group.get_Group_list()
    assert len(oldGroup) - 1 == len(newGroup)
    oldGroup[index:index+1] = []
    assert oldGroup == newGroup
