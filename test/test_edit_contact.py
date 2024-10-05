from model.contact import Contact


def test_modify_first_contact_name(app):
    app.contact.edit_first_contact(Contact(firstname="Betty"))

def test_modify_first_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname = "Anderson"))

def test_modify_first_contact_company(app):
    app.contact.edit_first_contact(Contact(company_name="Amazon"))

def test_modify_first_contact_mobile(app):
    app.contact.edit_first_contact(Contact(mobile="+13232423433"))

def test_modify_first_contact_email(app):
    app.contact.edit_first_contact(Contact(email="maria@amazon.com"))