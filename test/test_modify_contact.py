from model.contact import Contact


def test_modify_contact(app):
    data = Contact(firstname="Hello!")
    import pdb
    pdb.set_trace()
    contact = app.contact.modify_first_contact(data)
