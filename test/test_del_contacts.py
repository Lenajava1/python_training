

def test_delete_all_contacts(app):
    app.session.login()
    app.contact.delete_all_contacts()
    app.session.logout()