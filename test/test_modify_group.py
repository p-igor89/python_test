from model.group import Group


def test_modify_name_group(app):
    oldGroup = app.group.get_Group_list()
    group = Group(name='New Group')
    group.id = oldGroup[0].id
    app.group.modify_first_group(group)
    newGroup = app.group.get_Group_list()
    assert len(oldGroup) == len(newGroup)
    oldGroup[0] = group
    assert sorted(oldGroup, key=Group.idOrMax) == sorted(newGroup, key=Group.idOrMax)


# def test_modify_header_group(app):
#     oldGroup = app.group.get_Group_list()
#     app.group.modify_first_group(Group(header='New header'))
#     newGroup = app.group.get_Group_list()
#     assert len(oldGroup) == len(newGroup)
