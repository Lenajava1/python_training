from sys import maxsize

class Contact:

      def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company_name=None, address=None, mobile=None, workphone=None, homephone=None, fax=None, all_phones_from_home_page=None, email=None, email2=None, email3=None, all_emails_from_home_page=None, id=None):
            self.firstname = firstname
            self.middlename = middlename
            self.lastname = lastname
            self.nickname = nickname
            self.title = title
            self.company_name = company_name
            self.address = address
            self.mobile = mobile
            self.workphone = workphone
            self.homephone = homephone
            self.fax = fax
            self.email = email
            self.email2 = email2
            self.email3 = email3
            self.all_phones_from_home_page=all_phones_from_home_page
            self.all_emails_from_home_page = all_emails_from_home_page
            self.id = id

      def __repr__(self):
            return "%s: %s: %s: %s: %s: %s: %s: %s: %s: %s: %s: %s" % (self.id, self.lastname, self.middlename, self.firstname, self.nickname, self.title, self.company_name, self.address, self.mobile, self.homephone, self.workphone, self.email)

      def __eq__(self, other):
            return (self.id is None or other.id is None or self.id == other.id) and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

      def id_or_max(self):
            if self.id:
                  return int(self.id)
            else:
                  return maxsize