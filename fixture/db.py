import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name =name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name FROM group_list WHERE deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, name) = row
                list.append(Group(id=int(id), name=name))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, lastname, firstname, address FROM addressbook")
            for row in cursor:
                (id, lastname, firstname, address) = row
                list.append(Contact(id=int(id),lastname=lastname, firstname=firstname, address=address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()