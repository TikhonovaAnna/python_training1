from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test"))
    # data = Contact(firstname="Hello!")
    # import pdb
    # pdb.set_trace()
    # contact
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(firstname="Hello!")
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

