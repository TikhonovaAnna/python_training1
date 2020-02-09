import pymysql.cursors
from fixture.orm import ORMFixture
from model.group import Group


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# Извлечение информации из БД
try:
    # Получаем список контактов
    l = db.get_contacts_in_group(Group(id="788"))
    # Устраиваем итерацию
    for item in l:
        print(item)
    # Печатаем длину этот списка
    print(len(l))
finally:
    pass # db.destroy()