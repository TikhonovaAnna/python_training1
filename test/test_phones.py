import  re
from model.contact import Contact
from random import randrange
from fixture.db import DbFixture



def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_contact_data_on_db(app, db):
    contacts_from_ui = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i,  contacts in enumerate(contacts_from_ui):
        contact_from_db = contacts_from_db[i]
        assert contacts.firstname == contact_from_db.firstname
        assert contacts.lastname == contact_from_db.lastname
        #assert contacts.address == contact_from_db.address
        assert contacts.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contacts.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)


#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))