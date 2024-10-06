from model.contact import Contact

def test_delete_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer", company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru"))
    app.contact.delete_first_contact()