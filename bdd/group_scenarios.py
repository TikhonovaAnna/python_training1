from pytest_bdd import scenario
from .groups_steps import *


@scenario('groups.feature', 'Add new group')
def test_add_new_group():
    pass


@scenario('groups.feature', 'Delete a group')
def test_delete_some_group():
    pass


@scenario('groups.feature', 'Modify a group')
def test_group_modification():
    pass