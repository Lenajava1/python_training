from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login()
    app.contact.edit_first_contact(Contact(firstname="Maria", middlename="Ivanovna", lastname="Petrova", nickname="Masha", title="Programmer", company_name="Google", address="USA, New York", mobile="+1575757653", email="ivanova-masha@gmail.com"))
    app.session.logout()