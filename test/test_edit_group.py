import random
from model.group import Group



def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="my-group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.edit_group_by_id(group.id, Group(name="New_test_name", header="New_test_header", footer="New_test_footer"))
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    #old_groups[group.id] = group
    if check_ui:
       assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_modify_group_header(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name="my-group"))
    #old_groups = app.group.get_group_list()
    #app.group.edit_first_group(Group(header="modified_header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
