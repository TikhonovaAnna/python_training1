from model.contact import Contact
from random import randrange
import random
from model.group import Group


def test_add_contact_in_group(app, db):
    # Если нет контакта, то добавляем новый
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test_contact"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    # import pdb
    # pdb.set_trace()
    # Выбираем случайную группу
    old_groups = app.group.get_group_list()
    random_group = random.choice(old_groups)
    group_db_id = random_group.id
    # Выбираем случайный контакт, не состоящий в группе
    contacts_not_in_group = db.get_contact_not_in_group(group_db_id)
    random_contact = random.choice(contacts_not_in_group)
    random_contact_id = random_contact[0]
    old_contact_in_group = db.get_contact_in_group(group_db_id)
    app.contact.add_contact_to_group(random_contact_id, group_db_id)
    new_contacts_in_group = db.get_contact_in_group(group_db_id)
    assert len(old_contact_in_group) + 1 == len(new_contacts_in_group)
    assert (random_contact_id, group_db_id) in new_contacts_in_group

    # old_contacts = db.get_contact_list()
    # contact = random.choice(old_contacts)
    # #app.contact.add_contact_in_group(contact.id, contact.group_id)
    # groups = db.get_group_list()
    # group_id = random.choice(groups).id
    # app.contact.add_contact_in_group(contact.id, group_id)
    # new_contacts = db.get_contact_list(Group(id=group_id))
    # #assert len(old_contacts) == len(new_contacts)
    # #old_contacts[index] = contact
    # assert contact in new_contacts