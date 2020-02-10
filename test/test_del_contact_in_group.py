import random
from model.contact import Contact
from model.group import Group


def test_del_contact_in_group(app, db, check_ui):
    # Если нет контакта, то добавляем новый
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="del_contact_in_group"))
    if len(db.get_contact_list()) == 0:
        app.clcontact.add_contact(Contact(firstname="del_contact_in_group"))
    # Выбираем случайную группу
    old_groups = app.group.get_group_list()
    random_group = random.choice(old_groups)
    contact_not_in_group = db.get_contact_not_in_group(random_group)
    # ((563,),(643,))
    random_contact = random.choice(contact_not_in_group)
    # Выбираем первое поле(id) и полученной в виде tuple информации о контакте (843,)
    random_contact_id = random_contact[0]
    if len(db.get_contact_in_group(random_group.id)) == 0:
        app.contact.add_contact_to_group(random_contact_id, random_group.id)
    old_contact_in_group = db.get_contact_in_group(random_group.id)
    assert len(old_contact_in_group) != 0
    app.contact.del_contact_in_group(random_contact_id, random_group.id)
    new_contact_in_group = db.get_contact_in_group(random_group.id)
    assert len(old_contact_in_group) - 1 == len(new_contact_in_group)


    #contact = random.choice(old_contacts)
    #app.contact.del_contact_in_group(contact.id)
    #new_contacts = db.get_contact_list()
    # assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts.remove(contact)
    # assert old_contacts == new_contacts
    #assert old_contacts == new_contacts
    #if check_ui:
        #assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)