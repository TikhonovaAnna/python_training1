from model.group import Group
from random import randrange, choice


def test_modify_group_name(app, db, check_ui):
    # Проверяем, есть ли группы в базе
    if len(db.get_group_list()) == 0:
        # Если групп нет, создаём новую
        app.group.create(Group(name="test"))
    # Получаем список групп из базы
    old_groups = db.get_group_list()
    # Выбираем случайную группу для модификации
    index = randrange(len(old_groups))
    chosen_id = old_groups[index].id
    group = old_groups[index]
    # Описываем изменения в информации о группе
    group.name = "new_name"
    # Меняем информацию выбранной группы на новую
    app.group.modify_group_by_id(chosen_id, group)
    # Получаем список групп после изменения
    new_groups = db.get_group_list()
    # Проверяем, что количество групп не изменилось после модификации
    assert len(old_groups) == len(new_groups)
    # old_contacts[index] = contact
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="test"))
   # old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    # app.session.logout()
