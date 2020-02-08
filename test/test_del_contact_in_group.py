import random
from model.contact import Contact


def test_del_contact_in_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_in_group(contact.id)
    new_contacts = db.get_contact_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts.remove(contact)
    # assert old_contacts == new_contacts
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)