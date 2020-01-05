# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.application import Application
import pytest

from model.contact import Contact


def test_add_contact(app):
    # for _ in range(5):
        # app.open_home_page()
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="dsf", middlename="gdfg", lastname="ew", nickname="gdf", title="wer", company="dg",
                                address="dg", home="dg", mobile="43", work="sdg", fax="213", email="243", email2="234",
                                email3="245", homepage="fsdf", address2="dsf", phone2="sg", notes="sfghh")
        app.contact.add(contact)
        # app.return_home_page()
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def tearDown(self):
        # self.app.destroy()
