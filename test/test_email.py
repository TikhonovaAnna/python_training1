import re
from model.contact import Contact


def test_email_on_home_page(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    #contact_from_home_page = app.contact.get_contact_list(contact)

    new_contacts = db.get_contact_list()
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contact)
    assert contact.all_emails_from_home_page == old_contacts


# def test_emails_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.email == contact_from_edit_page.email
#    assert contact_from_view_page.email2 == contact_from_edit_page.email2
#    assert contact_from_view_page.email3 == contact_from_edit_page.email3


def clear(s):
    return re.sub("[()-]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                                    contact.email3]))))