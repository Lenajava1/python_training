from model.group import Group


def test_modify_group_name(app):
    app.session.login()
    app.group.edit_first_group(Group(name="modified_group_name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login()
    app.group.edit_first_group(Group(header="modified_header"))
    app.session.logout()
