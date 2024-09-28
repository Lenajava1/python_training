from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.contact import ContactHelper
from fixture.session2 import Session2Helper


class SuperTest:

      def __init__(self):
          self.wd = WebDriver()
          self.wd.implicitly_wait(30)
          self.session2 = Session2Helper(self)
          self.contact = ContactHelper(self)

      def open_home_page(self):
          wd = self.wd
          wd.get("http://localhost/addressbook/edit.php")

      def destroy(self):
          self.wd.quit()
