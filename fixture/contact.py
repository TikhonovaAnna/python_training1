from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")
#        wd.find_element_by_link_text("add new").click()

    def add(self, contact):
        wd = self.app.wd
        # open contact
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        # add contact
        self.fill_contact_form(contact)
        # submit contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def delete_first_contact(self):
        wd = self.app.wd
        # self.open_home_page()
        wd.get("http://localhost/addressbook/")
        # select first group
        # wd.find_element_by_link_text("selected[]").click()
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        # wd.find_element_by_link_text("delete[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = self.app.wd.switch_to_alert()
        alert.accept()
        del_text = wd.find_element_by_xpath("//div[@class='msgbox']").text
        assert del_text == 'Record successful deleted'
        # self.app.wd.switch_to_alert.accept()
        # self.return_home_page()
        # wd.get("http://localhost/addressbook/")

    def open_edit(self):
        self.app.wd.get("http://localhost/addressbook/")
        self.app.wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def fill_name(self, name):
        self.app.wd.find_element_by_name("firstname").click()
        self.app.wd.find_element_by_name("firstname").clear()
        self.app.wd.find_element_by_name("firstname").send_keys(name)

    def update(self):
        self.app.wd.find_element_by_xpath("(//input[@name='update'])[2]").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("home page").click()
        self.app.wd.find_element_by_link_text("Logout").click()

    # def check(self):
        # pass

    def modify_first_contact(self, contact: Contact):
        self.open_edit()
        #self.fill_name(contact.firstname)
        self.fill_contact_form(contact)
        self.update()
        # self.check()
        self.logout()

        #wd = self.app.wd
        #wd.get("http://localhost/addressbook/")
        #wd.find_element_by_name("selected[]").click()
        #self.open_groups_page()
        #self.select_first_group()
        # open modification form
        #wd.find_element_by_name("edit").click()
        # fill group form
        #self.fill_group_form(new_group_date)
        # submit modification
        #wd.find_element_by_name("update").click()
        #self.return_to_groups_page()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()