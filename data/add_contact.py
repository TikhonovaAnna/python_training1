from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname, middlename="fghjjf", lastname=lastname, nickname="xhel",
            title="contact", company="xshel", address="addrfess", home="768867876", mobile="+79445",
            work="546", fax="43232", email="teretr@ty.ty", email2="gfhf@hg.nb", email3="87dsuf@yu.ru",
            homepage="http://tsdjf.ua", address2="gddjkjghg d-5. kv7", phone2="city",
            notes="ghfgfhfhfhfgg")
    for firstname in ["", random_string("firstname", 5)]
    for address in ["", random_string("address", 7)]
    for lastname in ["", random_string("lastname", 9)]
]