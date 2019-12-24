from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname="test"))
    # data = Contact(firstname="Hello!")
    # import pdb
    # pdb.set_trace()
    #contact =\
        app.contact.modify_first_contact(firstname="Hello!")

