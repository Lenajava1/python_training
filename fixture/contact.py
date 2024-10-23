from gettext import gettext
from operator import index

from selenium.webdriver.common.by import By

from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements(By.LINK_TEXT, "add next")) > 0):
            wd.find_element(By.LINK_TEXT, "home page").click()

    def return_to_home(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact()
        # fill contact form
        self.fill_contact_form(contact)
        # Submit the form
        wd.find_element(By.XPATH, "//input[@type='submit']").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        self.select_contact_by_index(index)
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.XPATH, "//input[@type='checkbox']")[index].click()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.return_to_home()
        wd.find_element(By.ID, "MassCB").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.find_element(By.XPATH, "//a[contains(text(),'home')]").click()
        self.contact_cache = None

    def edit_first_contact(self,new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        # open edit form
        self.select_edit_by_index(1)
        #fill contact form
        self.fill_contact_form(new_contact_data)
        #submit form
        wd.find_element(By.XPATH, "(//input[@name='update'])[1]").click()
        self.return_to_home()
        self.contact_cache = None


    def select_edit_by_index(self,index):
        wd = self.app.wd
        self.return_to_home()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        # open edit form
        self.select_edit_by_index(index)
        #fill contact form
        self.fill_contact_form(new_contact_data)
        #submit form
        wd.find_element(By.XPATH, "(//input[@name='update'])[1]").click()
        self.return_to_home()
        self.contact_cache = None

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.select_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        middlename = wd.find_element(By.NAME, "middlename").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        nickname =wd.find_element(By.NAME, "nickname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        fax = wd.find_element(By.NAME, "fax").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        return Contact(id=id, lastname=lastname, middlename=middlename, nickname=nickname,
                       firstname=firstname, homephone=homephone, workphone=workphone, mobile=mobile,
                       email=email, email2=email2, email3=email3, address=address, fax=fax)

    def get_contact__from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        fax = re.search("F: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone, mobile=mobile, fax=fax)



    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements(By.XPATH, "//tr[@name='entry']"))

    contact_cache= None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                last_name = cells[1].text
                first_name = cells[2].text
                address = cells[3].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text
                all_emails_from_home_page = cells[4].text
                self.contact_cache.append(Contact(id=id, lastname=last_name, firstname=first_name, address=address,
                                                  all_emails_from_home_page=all_emails_from_home_page,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)






