class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, userName, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(userName)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensureLogout(self):
        wd = self.app.wd
        if self.isLoggedIn():
            self.logout()

    def isLoggedInAs(self, username):
        wd = self.app.wd
        return wd.find_element_by_id("theMainUserName").text == "("+username+")"

    def isLoggedIn(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensureLogin(self, userName, password):
        if self.isLoggedIn():
            if self.isLoggedInAs(userName):
                return
            else:
                self.logout()
        self.login(userName, password)
