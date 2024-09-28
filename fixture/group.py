from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        wd.find_element(By.NAME, "group_name").clear()
        # fill group form
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #select group
        wd.find_element(By.NAME, "selected[]").click()
        #submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_group_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element(By.XPATH, "(//input[@name='selected[]'])[1]").click()
        wd.find_element(By.NAME, "edit").click()
        wd.find_element(By.NAME, "group_name").clear()
        # edit group form
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # Update group edition
        wd.find_element(By.NAME, "update").click()
        self.return_to_group_page()



