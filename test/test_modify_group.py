from model.group import Group
import random


def test_modify_group_name(app, db):
    #if app.group.count() == 0:
    # Проверяем, есть ли группы в базе
    if not db.get_group_list():
        # Если групп нет, создаём новую
        app.group.create(Group(name="test"))
    # Получаем список групп из базы
    groups = db.get_group_list()
    # Выбираем случайную группу для модификации
    chosen_group = random.choice(groups)
    #index = randrange(len(old_groups))
    # Описываем изменения в информации о группе
    new_group_data = Group(name="New group")
    new_group_data.id = chosen_group.id
    # Меняем информацию выбранной группы на новую
    app.group.modify_group_by_id(chosen_group.id, new_group_data)
    # Получаем список групп после изменения
    new_groups = db.get_group_list()

    # Проверяем, что количество групп не изменилось после модификации
    assert len(groups) == len(new_groups)

    # for i in range(len(new_groups)):
    #    if groups[i].id == chosen_group.id:
    #        new_groups[i] = new_group_data

    # Проверяем, что поменялась информация только в изменяемой группе.
    for group, new_group in zip(groups, new_groups):
        if group.id != chosen_group.id:
            assert group == new_group
        else:
            assert new_group.name == new_group_data.name
    #app.session.logout()


#def test_modify_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="test"))
   # old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="New header"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    # app.session.logout()
