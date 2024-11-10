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
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=int(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, email FROM addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, email) = row
                list.append(Contact(id=int(id),firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, company_name=company, title=title, address=address, homephone=home, mobile=mobile, workphone=work, email=email))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()