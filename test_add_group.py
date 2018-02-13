# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_app_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "secret", "admin")
        self.open_group_page(wd)
        self.create_group(wd, "Example", "Address", "Notes")
        self.retorn_to_group_page(wd)
        self.logout(wd)

    def test_app_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, "secret", "admin")
        self.open_group_page(wd)
        self.create_group(wd, "", "", "")
        self.retorn_to_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def retorn_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, name, header, footer):
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group film
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, password, userName):
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(userName)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
