# -*- coding: utf-8 -*-
from model.group import Group


def test_app_group(app):
    oldGroup = app.group.get_Group_list()
    group = Group("Example", "Address", "Notes")
    app.group.create(group)
    assert len(oldGroup) + 1 == app.group.count()
    newGroup = app.group.get_Group_list()
    oldGroup.append(group)
    assert sorted(oldGroup, key=Group.idOrMax) == sorted(newGroup, key=Group.idOrMax)


# def test_app_empty_group(app):
#     oldGroup = app.group.get_Group_list()
#     group = Group("", "", "")
#     app.group.create(group)
#     newGroup = app.group.get_Group_list()
#     assert len(oldGroup) + 1 == len(newGroup)
#     oldGroup.append(group)
#     assert sorted(oldGroup, key=Group.idOrMax) == sorted(newGroup, key=Group.idOrMax)
