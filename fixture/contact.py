from model.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("home").click()
        # wd.get("http://localhost/addressbook/")
        # wd.find_element_by_link_text("add new").click()

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def add(self, contact):
        wd = self.app.wd
        # open contact
        self.open_home_page()
        wd.find_element_by_link_text("add new").click()
        # add contact
        self.fill_contact_form(contact)
        # submit contact
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        # self.return_to_home_page()
        self.contact_cache = None

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

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # wd.get("http://localhost/addressbook/")
        # select first group
        self.select_contact_by_index(index)
        # wd.find_element_by_link_text("selected[]").click()
        # wd.find_element_by_name("selected[]").click()
        # submit deletion
        # wd.find_element_by_link_text("delete[]").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        alert = self.app.wd.switch_to_alert()
        alert.accept()
        self.contact_cache = None
        # del_text = wd.find_element_by_xpath("//div[@class='msgbox']").text
        # assert del_text == 'Record successful deleted'
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
        self.contact_cache = None

    def logout(self):
        self.app.wd.find_element_by_link_text("home page").click()
        self.app.wd.find_element_by_link_text("Logout").click()

    # def check(self):
        # pass

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data: Contact):
        wd = self.app.wd
        # -- self.open_edit()
        self.open_home_page()
        # self.fill_name(contact.firstname)
        # import pdb;
        # pdb.set_trace()
        # self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        self.update()
        # self.check()
        # self.logout()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    # contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                # -- text = element.text
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)

