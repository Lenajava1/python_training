# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.super_test import SuperTest

@pytest.fixture()
def super_test(request):
    fixture = SuperTest()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(super_test):
        super_test.session2.login(username="admin", password="secret")
        super_test.create_contact(Contact(firstname="Elena", middlename="Evgenievna", lastname="Mutykova", nickname="Lena", title="QA Engineer", company_name="VirtoCommerce", address="Hungary, Budapest", mobile="+3665765675675", email="mutykovaelena@gmail.com"))
        super_test.session2.logout()

