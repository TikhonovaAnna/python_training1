from model.contact import Contact
from random import randrange
import random
from model.group import Group


def test_add_contact_in_group(app, db):
    # Выполняем предусловия
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # Выбираем рандомную группу
    old_groups = app.group.get_group_list()
    #group = random.choice(old_groups)
    #old_contacts = app.contact.get_contact_list()
    random_group = random.choice(old_groups)
    group_db_id = random_group.id
    # выбираем рандомный контакт, не состоящий в группе
    contact_not_in_group = db.get_contact_not_in_group(group_db_id)
    # если все клиенты уже состоят в выбранной группе добавляем нового клиента
    #if len(contact_not_in_group) == 0:
        #app.client.add_contact(Contact(firstname="new_contact_in_group"))
    # выбираем клиента из тех, которые еще не состоят в выбранной группе
    #add_contact_in_group = app.client.add_client_to_group(contact_not_in_group, group)
    random_contact = random.choice(contact_not_in_group)
    #assert add_contact_in_group in db.get_contact_in_group(group)
    old_contact_in_group = db.get_contact_in_group(group_db_id)
    app.contact.add_contact_to_group(random_contact, random_group)
    new_contacts_in_group = db.get_contact_in_group(group_db_id)
    assert len(old_contact_in_group) == len(new_contacts_in_group) + 1

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