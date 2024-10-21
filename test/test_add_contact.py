# -*- coding: utf-8 -*-
from itertools import count

from model.contact import Contact

def test_add_contact(app):
    contact = Contact(firstname="Elena", middlename="Evgenievna", lastname="Mutykova", nickname="Lena", title="QA Engineer", company_name="VirtoCommerce", address="Hungary, Budapest", mobile="+3665765675675", email="mutykovaelena@gmail.com")
    if app.contact.count() == 0:
       app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


