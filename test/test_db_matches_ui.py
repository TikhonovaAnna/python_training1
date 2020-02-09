from model.group import Group
from timeit import timeit
from model.contact import Contact


def test_group_list(app, db):
    #print(timeit(lambda: app.group.get_group_list(), number=1))
    ui_list = app.group.get_group_list()
    def clean(group):
       return Group(id=group.id, name=group.name.strip())
    #print(timeit(lambda: map(clean, db.get_group_list()), number=1000))
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
    #assert False

#def test_addressbook(app, db):
#    print(timeit(lambda: app.contact.get_contact_list(), number=1))
#    def clean(contact):
#        return Contact(id=contact.id, firstname=contact.firstname.strip())
#    print(timeit(lambda: map(clean, db.get_contact_list()), number=1000))
#    assert False #sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)