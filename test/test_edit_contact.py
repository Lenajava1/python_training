from model.contact import Contact


def test_modify_first_contact_name(app):
    app.session.login()
    app.contact.edit_first_contact(Contact(firstname="Betty", lastname="Anderson", nickname="Bet"))
    app.session.logout()

def test_modify_first_contact_company(app):
    app.session.login()
    app.contact.edit_first_contact(Contact(company_name="Amazon"))
    app.session.logout()

def test_modify_first_contact_mobile(app):
    app.session.login()
    app.contact.edit_first_contact(Contact(mobile="+13232423433"))
    app.session.logout()

def test_modify_first_contact_email(app):
    app.session.login()
    app.contact.edit_first_contact(Contact(email="maria@amazon.com"))
    app.session.logout()