from selenium.webdriver.common.by import By

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

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company_name)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home()
        self.select_first_contact()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "(//input[@type='checkbox'])[1]").click()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.return_to_home()
        wd.find_element(By.ID, "MassCB").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.find_element(By.XPATH, "//a[contains(text(),'home')]").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        self.select_first_contact()
        # open edit form
        wd.find_element(By.XPATH,"(//img[@title='Edit'])[1]").click()
        #fill contact form
        self.fill_contact_form(new_contact_data)
        #submit form
        wd.find_element(By.XPATH, "(//input[@name='update'])[1]").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.return_to_home()
        return len(wd.find_elements(By.XPATH, "//input[@type='checkbox']")) > 1




