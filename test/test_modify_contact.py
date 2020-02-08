from model.contact import Contact
from random import randrange, choice


#def test_modify_contact2(app, db):
    # if app.contact.count() == 0:
#    if len(db.get_contact_list()) == 0:
#        app.contact.add(Contact(firstname="test"))
    # data = Contact(firstname="Hello!")
    # import pdb
    # pdb.set_trace()
    # contacth
#    old_contacts = db.get_contact_list()
#    index = randrange(len(old_contacts))
#    chosen_id = old_contacts[index].id
#    contact = old_contacts[index]
#    contact.firstname = "Hello2!"
    # contact = Contact(firstname="Hello!")
    # contact.id = old_contacts[index].id
    # contact.lastname = old_contacts[index].lastname
#    app.contact.modify_contact_by_id(chosen_id, contact)
#    new_contacts = db.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
    # old_contacts[index] = contact
#    assert old_contacts == new_contacts
    # assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact(app, db):
    if not db.get_contact_list():
        app.contact.add(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    old_contacts[index].firstname = "Hello3!"
    app.contact.modify_contact_by_id(old_contacts[index].id, old_contacts[index])
    # contact = choice(old_contacts)
    # contact.firstname = "Hello2!"
    #app.contact.modify_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert old_contacts == new_contacts
