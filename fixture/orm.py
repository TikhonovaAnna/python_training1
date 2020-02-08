from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders


class ORMFixture:
    
    # Делаем переменную уровня класса
    db = Database()
    
    # Привязка описывается в виде набора классов
    class ORMGroup(db.Entity):
        # Указываем название таблицы
        _table_ = 'group_list'
        # Внутри класса описываем набор св-в и привязываем к полям таблицы (в качестве параметра тип поля в БД) 
        id = PrimaryKey(int, column='group_id')
        # Optional - так как это поле необязательное, может быть пустым 
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')

    # Описываем привязку к БД
    def __init__(self, host, name, user, password):
        # привязка (параметры: тип БД,набор параметров в таком же виде,как это передается при инициализации коннектора)
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders)
        # сопоставление св-в, описанных классов с таблтцами и полями этих таблтц)
        self.db.generate_mapping()
        # Чтоб увидеть реальные запросы на языке SQL, которые автоматически создаются
        sql_debug(True)

    def convert_groups_to_model (self, groups):
        # вспомошательная ф-ция, конвертирующая одну отдельно взятую группу
        def convert(group):
            # строим новый объект типа Group со свойствами... Идентификаторы будут строками
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        # преобразование объектов
        return list(map(convert, groups))

    # Сессия: 1 вариант
    # @db_session
    # реалтзовывем ф-ции, которые получают списки объектов
    def get_group_list(self):
        # Этот плок кода должен выполняться в виде сессии. Сессия откр и закр автоматически. 2 вариант
        with db_session:
            # Делаем выборку из набора объектов соответствующего класса. Выбираются данные
            # из табл и автомат преобразуются в объекты этого класса. В качестве параметра класса передаем
            # конструкцию типалист компрехеншн. Запрос преобразовывем в список из объектов типа ORMGroup в
            # наши модельные объекты
            return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        with db_session:
            # выбрать все строки, где поле deprecated не заполнено
            return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))
