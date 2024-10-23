from selenium.webdriver.common.by import By

class SessionHelper:

     def __init__(self, app):
         self.app = app

     def login(self, username, password):
         wd = self.app.wd
         self.app.open_home_page()
         wd.find_element(By.NAME, "user").click()
         wd.find_element(By.NAME, "user").clear()
         wd.find_element(By.NAME, "user").send_keys(username)
         wd.find_element(By.NAME, "pass").clear()
         wd.find_element(By.NAME, "pass").send_keys(password)
         wd.find_element(By.XPATH, '//input[@value="Login"]').click()

     def logout(self):
         wd = self.app.wd
         wd.find_element(By.NAME, "logout").click()
         #wd.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()

     def ensure_logout(self):
         wd = self.app.wd
         if self.is_logged_in():
            self.logout()

     def is_logged_in(self):
         wd = self.app.wd
         return len(wd.find_elements(By.NAME, "logout")) > 0

     def get_user_name(self):
         wd = self.app.wd
         return wd.find_element(By.XPATH, "//div/div[1]/form/b").text[1:-1]

     def is_logged_in_as(self, username):
         return self.get_user_name == username

     def ensure_login(self, username, password):
         wd = self.app.wd
         if self.is_logged_in():
             if self.is_logged_in_as(username):
                 return
             else:
                 self.logout()
         self.login(username, password)



