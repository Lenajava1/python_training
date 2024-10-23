
from model.contact import Contact

def test_emails_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="Lastname1", middlename="", nickname="Nick", title="Developer",
                    company_name="Yandex", address="", mobile="+793242543253", email="nick@yandex.ru", email2="", email3="nick2424@index.ru"))
    index = app.contact.count()
    contact_from_home_page = app.contact.get_contact_list()[index-1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index-1)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             filter( lambda x: x is not None,
                                        [contact.email, contact.email2, contact.email3])))