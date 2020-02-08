import pymysql.cursors
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
# Извлечение информации из БД
try:
    # Получаем список контактов
    l = db.get_contact_list()
    # Устраиваем итерацию
    for item in l:
        print(item)
    # Печатаем длину этот списка
    print(len(l))
finally:
    pass # db.destroy()