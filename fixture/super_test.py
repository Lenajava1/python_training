from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fixture.session2 import Session2Helper


class SuperTest:

      def __init__(self):
          self.wd = WebDriver()
          self.wd.implicitly_wait(30)
          self.session2 = Session2Helper(self)


      def create_contact(self, contact):
          wd = self.wd
          # Add new contact
          wd.find_element(By.LINK_TEXT, "add new").click()
          # fill contact form
          wd.find_element(By.NAME, "firstname").clear()
          wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
          wd.find_element(By.NAME, "middlename").clear()
          wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
          wd.find_element(By.NAME, "lastname").clear()
          wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
          wd.find_element(By.NAME, "nickname").clear()
          wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
          wd.find_element(By.NAME, "title").clear()
          wd.find_element(By.NAME, "title").send_keys(contact.title)
          wd.find_element(By.NAME, "company").clear()
          wd.find_element(By.NAME, "company").send_keys(contact.company_name)
          wd.find_element(By.NAME, "address").clear()
          wd.find_element(By.NAME, "address").send_keys(contact.address)
          wd.find_element(By.NAME, "mobile").clear()
          wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
          wd.find_element(By.NAME, "email").clear()
          wd.find_element(By.NAME, "email").send_keys(contact.email)
          # Select birthdate
          Select(wd.find_element(By.NAME, "bday")).select_by_visible_text("1")
          Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text("April")
          wd.find_element(By.NAME, "byear").clear()
          wd.find_element(By.NAME, "byear").send_keys("1994")
          # Submit the form
          wd.find_element(By.XPATH, "//input[@type='submit']").click()


      def open_home_page(self):
          wd = self.wd
          wd.get("http://localhost/addressbook/edit.php")

      def destroy(self):
          self.wd.quit()
