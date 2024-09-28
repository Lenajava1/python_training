# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login()
    app.contact.create(Contact(firstname="Elena", middlename="Evgenievna", lastname="Mutykova", nickname="Lena", title="QA Engineer", company_name="VirtoCommerce", address="Hungary, Budapest", mobile="+3665765675675", email="mutykovaelena@gmail.com"))
    app.session.logout()

