from selenium.webdriver.common.by import By

class Session2Helper:

    def __init__(self, super_test):
        self.super_test = super_test

    def login(self, username, password):
        wd = self.super_test.wd
        self.super_test.open_home_page()
        # Login
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.super_test.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()