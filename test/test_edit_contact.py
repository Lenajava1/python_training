from model import contact
from model.contact import Contact


def test_modify_first_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="Betty"))
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(old_contacts)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_first_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    app.contact.edit_first_contact(Contact(lastname = "Anderson"))
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(old_contacts)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_first_contact_company(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    app.contact.edit_first_contact(Contact(company_name="Amazon"))

def test_modify_first_contact_mobile(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    app.contact.edit_first_contact(Contact(mobile="+13232423433"))

def test_modify_first_contact_email(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    app.contact.edit_first_contact(Contact(email="maria@amazon.com"))