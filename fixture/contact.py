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
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

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
        self.fill_name(contact.firstname)
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