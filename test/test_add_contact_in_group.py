from model.contact import Contact
from random import randrange
import random
from model.group import Group


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #app.contact.add_contact_in_group(contact.id, contact.group_id)
    groups = db.get_group_list()
    group_id = random.choice(groups).id
    app.contact.add_contact_in_group(contact.id, group_id)
    new_contacts = db.get_contact_list(Group(id=group_id))
    #assert len(old_contacts) == len(new_contacts)
    #old_contacts[index] = contact
    assert contact in new_contacts