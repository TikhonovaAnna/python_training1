#import pymysql.connection
import pymysql.cursors
from model.group import Group
from model.contact import Contact
import pymysql.cursors


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
            cursor.execute("select id, firstname, lastname, email, email2, email3, address from addressbook where deprecated='0000-00-00 00:00:00'")
            # Итерация для строки
            for row in cursor:
                # Три переменные, в которые помещаются значения из кортежа, соответствующего каждой строке
                (id, firstname, lastname, email, email2, email3, address) = row
                # Создаем контакт с заданным идегтификатороми
                list.append(Contact(id=id, firstname=firstname, lastname=lastname,
                                    email=email, email2=email2, email3=email3,
                                    address=address))
        finally:
            cursor.close()
        return list

    def get_contact_in_group(self, group_id):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute(
                "select id, group_id from address_in_groups where group_id=%s",
                (int(group_id),)
            )
            return cursor.fetchall()
            # row = cursor.fetchone()
            # list.append(row)
        finally:
            cursor.close()
        # return list

    def get_contact_not_in_group(self, group_id):
        cursor = self.connection.cursor()
        list = []
        try:
            # cursor.execute(
            #    "select id, group_id from address_in_groups left join addressbook on id=id "
            #    "where group_id is None", str(group_id))
            ## select address_in_groups.id, group_id from address_in_groups left join addressbook on address_in_groups.id=addressbook.id where group_id is NULL
            cursor.execute(
                "select ab.id from addressbook ab "
                "LEFT JOIN address_in_groups ag on ab.id = ag.id where ag.group_id is NULL"
            )
            return cursor.fetchall()
        finally:
            cursor.close()

    def destroy(self):
        self.connection.close()