# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
        app.open_home_page()
        app.login(username="admin", password="secret")
        app.add_contact(Contact(firstname="dsf", dlename="gdfg", lastname="ew", nickname="gdf", title="wer", company="dg",
                         address="dg", home="dg", mobile="43", work="sdg", fax="213", email="243", email2="234",
                         email3="245", homepage="fsdf", address2="dsf", phone2="sg", notes="sfghh"))
        app.return_home_page()
        app.logout()

    
def tearDown(self):
        self.app.destroy()
