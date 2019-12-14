# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    app.contact.add(Contact(firstname="dsf", dlename="gdfg", lastname="ew", nickname="gdf", title="wer", company="dg",
                            address="dg", home="dg", mobile="43", work="sdg", fax="213", email="243", email2="234",
                            email3="245", homepage="fsdf", address2="dsf", phone2="sg", notes="sfghh"))
    app.return_home_page()


def tearDown(self):
        self.app.destroy()
