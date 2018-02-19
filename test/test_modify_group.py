from model.group import Group
from random import randrange


def test_modify_name_group_by_index(app):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    oldGroup = app.group.get_Group_list()
    index = randrange(len(oldGroup))
    group = Group(name='New Group')
    group.id = oldGroup[index].id
    app.group.modify_group_by_index(index, group)
    newGroup = app.group.get_Group_list()
    assert len(oldGroup) == len(newGroup)
    oldGroup[index] = group
    assert sorted(oldGroup, key=Group.idOrMax) == sorted(newGroup, key=Group.idOrMax)


# def test_modify_header_group(app):
#     oldGroup = app.group.get_Group_list()
#     app.group.modify_first_group(Group(header='New header'))
#     newGroup = app.group.get_Group_list()
#     assert len(oldGroup) == len(newGroup)
