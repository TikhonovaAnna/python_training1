Scenario Outline: Add new group
    # ппредусловие
    Given a group list
    Given a group with <name>, <header> and <footer>
    # действие
    When I add a new group to the list
    # результат
    Then the new group list is equal to the old list with the added group

    Examples:
    | name  | header  | footer  |
    | name1 | header1 | footer1 |
    | name2 | header2 | footer2 |



Scenario: Delete a group
    Given a non-empty group list
    Given a random group from the list
    When I delete the group from list
    Then the new group list is equal to the old list without the delete group


Scenario: Modify a group
    Given a non-empty group list
    Given a random group from the list
    When I modify the group from list
    Then the new group list is equal to the old list