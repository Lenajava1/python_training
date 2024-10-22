# -*- coding: utf-8 -*-
from itertools import count

from model.contact import Contact

def test_add_contact(app):
    contact = Contact(firstname="Elena", middlename="Evgenievna", lastname="Mutykova", nickname="Lena", title="QA Engineer", company_name="VirtoCommerce", address="Hungary, Budapest", mobile="+3665765675675", homephone="232-23-23", workphone="(31)31-134-33", fax="67676-228(0)", email="mutykovaelena@gmail.com")
    if app.contact.count() == 0:
       app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


