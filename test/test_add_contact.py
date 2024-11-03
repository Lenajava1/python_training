# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", middlename="", nickname="", title="", company_name="", address="", homephone="", workphone="", fax="", email="")] + [
Contact(firstname=random_string("firstname", 5),
        lastname=random_string("lastname", 10),
        middlename=random_string("middlename", 8),
        nickname=random_string("nickname", 3),
        title=random_string("title", 8),
        company_name=random_string("company", 16),
        address=random_string("address", 20),
        mobile=random_string("", 10),
        homephone=random_string("", 10),
        workphone=random_string("", 12),
        email=random_string("", 8))

for i in range(5)

]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    #if app.contact.count() == 0:
       #app.contact.create(contact)
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


