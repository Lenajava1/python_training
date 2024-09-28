

def test_delete_all_contacts(app):
    app.session.login()
    app.contact.delete_first_contact()
    app.session.logout()