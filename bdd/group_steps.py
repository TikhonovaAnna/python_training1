from pytest_bdd import given, when, then
from model.group import Group
import random


@given('a group list')
# старый список групп
def group_list(db):
    return db.get_group_list()


@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@when('I add a new group to the list')
def add_new_group(app, new_group):
    app.group.create()
    app.group.fill_group_form(new_group)
    app.group.submit_group_creation()


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create()
        app.group.fill_group_form(Group(name="Some name"))
        app.group.submit_group_creation()
    return db.get_group_list()


@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old list without the delete group')
def verify_group_delete(db, non_empty_group_list, random_group, app, check_ui):
    new_groups = db.get_group_list()
    assert len(non_empty_group_list) - 1 == len(new_groups)
    non_empty_group_list.remove(random_group)
    assert non_empty_group_list == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


@when('I modify the group from list')
def group_modification(app, random_group):
    app.group.modify_group_by_id(random_group.id, Group(name="Modified group"))


@then('the new group list is equal to the old list')
def verification_list_groups_are_the_same(db, non_empty_group_list, check_ui, app):
    assert len(non_empty_group_list) == app.group.count()
    new_groups = db.get_group_list()
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)