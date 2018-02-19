from model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        self.fill_group(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.groupCache = None

    def fill_group(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def del_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # Delete group
        wd.find_element_by_name("delete").click()
        # Submit group creation
        self.return_to_group_page()
        self.groupCache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # Edit group
        wd.find_element_by_name("edit").click()
        # Modify group
        self.fill_group(new_group_data)
        # Submit notification
        wd.find_element_by_name("update").click()
        # Submit group creation
        self.return_to_group_page()
        self.groupCache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    groupCache = None

    def get_Group_list(self):
        if self.groupCache is None:
            wd = self.app.wd
            self.open_group_page()
            self.groupCache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.groupCache.append(Group(name=text, id=id))
        return list(self.groupCache)
