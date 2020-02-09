#import pymysql.connection
import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):   # метод, который загружает инфо из БД о группах
        list = []
        cursor=self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    # Метод для загрузки контактов из БД
    def get_contact_list(self):
        list = []
        # Получаем курсор
        cursor = self.connection.cursor()
        try:
            # Выполняем запрос
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            # Итерация для строки
            for row in cursor:
                # Три переменные, в которые помещаются значения из кортежа, соответствующего каждой строке
                (id, firstname, lastname) = row
                # Создаем контакт с заданным идегтификатороми
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()