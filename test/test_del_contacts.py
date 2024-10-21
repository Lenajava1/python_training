from model.contact import Contact
from random import randrange

def test_delete_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts [index:index+1] = []
    assert old_contacts == new_contacts