from model.contact import Contact
from random import randrange


def test_modify_contact(app, db):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test"))
    # data = Contact(firstname="Hello!")
    # import pdb
    # pdb.set_trace()
    # contact
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Hello!")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

