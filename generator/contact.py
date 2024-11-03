import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys


def print_usage():
    pass


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    print_usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
        if o == "-n":
            n = int(a)
        elif o == "-f":
            f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_telephone(prefix, maxlen):
    symbols = string.digits*20
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen1,maxlen2):
    characters = string.ascii_lowercase + string.digits
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    username = ''.join(random.choices(characters, k=random.randint(maxlen1,maxlen2)))
    domain = random.choice(domains)
    return f"{username}@{domain}"


testdata = [Contact(firstname="", lastname="", middlename="", nickname="", title="", company_name="", address="", homephone="", workphone="", fax="", email="")] + [
Contact(
    firstname=random_string("firstname", 6),
    lastname=random_string("lastname", 10),
    middlename=random_string("middlename", 8),
    nickname=random_string("nickname", 3),
    title=random_string("title", 8),
    company_name=random_string("company", 16),
    address=random_string("address", 20),
    mobile=random_telephone("+36", 15),
    homephone=random_telephone("(323)", 15),
    workphone=random_telephone("8(922)", 15),
    email=random_email(5, 10))

for i in range(n)

]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))