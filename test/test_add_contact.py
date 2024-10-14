# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", middlename="Evgenievna", lastname="Mutykova", nickname="Lena", title="QA Engineer", company_name="VirtoCommerce", address="Hungary, Budapest", mobile="+3665765675675", email="mutykovaelena@gmail.com")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


