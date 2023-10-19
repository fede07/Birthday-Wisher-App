##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

MAX_TEMPLATES = 3

import random
import smtplib
import datetime as dt
import pandas

my_email = "dummy@gmail.com"
password = "testingpass"

today = dt.datetime.now()
today_tuple = (today.day, today.month)

data = pandas.read_csv("birthdays.csv")
birthdays_dic = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows() }

if today_tuple in birthdays_dic:

    choice = random.randint(1, MAX_TEMPLATES)
    file = f"letter_templates\letter_{choice}.txt"
    birthday_person = birthdays_dic[today_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]
    
    print(name)

    letter_content = None

    with open(file=file) as letter:
        letter_content = letter.read()
        letter_content = letter_content.replace("[NAME]", name)
        print(letter_content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs= email,
            msg=letter_content
        )