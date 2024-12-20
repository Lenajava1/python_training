from operator import index
import random
from model.contact import Contact
from random import randrange


def test_modify_some_contact_name(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #contact.id = old_contacts[index].id
    app.contact.edit_contact_by_id(contact.id, Contact(firstname="Betty", lastname="Swanson", middlename="Van", nickname="Bat", title="QA", company_name="Y-bank", address="CA, Avenue Bay 122/A, 44444", mobile="89898966666", email="betty-swanson@yahooo.com"))
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    if check_ui:
       assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_modify_some_contact_lastname(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    #old_contacts = app.contact.get_contact_list()
    #index = randrange(len(old_contacts))
    #contact = Contact(lastname = "Anderson")
    #contact.id = old_contacts[index].id
    #app.contact.edit_contact_by_index(index, contact)
    #assert len(old_contacts) == app.contact.count()
    #new_contacts = app.contact.get_contact_list()
    #old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_first_contact_company(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    #app.contact.edit_first_contact(Contact(company_name="Amazon"))

#def test_modify_first_contact_mobile(app):
    #if app.contact.count() == 0:
       # app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    #app.contact.edit_first_contact(Contact(mobile="+13232423433"))

#def test_modify_first_contact_email(app):
    #if app.contact.count() == 0:
        #app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    #app.contact.edit_first_contact(Contact(email="maria@amazon.com"))