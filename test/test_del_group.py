

def test_delete_first_group(app):
    app.session.login()
    app.group.delete_first_group()
    app.session.logout()