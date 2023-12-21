import datetime as dt
import pandas
import random
import smtplib

# inputs
your_name = "XXX"          # Update your name here
my_email = "XXX@gmail.com" # Update your email here
password = "XXX"           # update your password here

# find today's date
today = dt.datetime.now()
month = today.month
day = today.day

# open CSV file of birthdays (name,email,year,month,day)
# create dictionary of (month, day) : data_row
birthday = {}
file = pandas.read_csv("birthdays.csv")
for index, row in file.iterrows():
    birthday[(row.month, row.day)] = birthday.get((row.month, row.day), [])
    birthday[(row.month, row.day)].append(row)

# check if birthday in dictionary
# if yes, choose email template and send
if (month, day) in birthday:
    list_of_people = birthday[(month, day)]
    for person in list_of_people:
        random_int = random.randint(1, 3)
        name = person["name"]
        email = person["email"]
        with open(f"./letter_templates/letter_{random_int}.txt") as letter:
            content = letter.read()
            content = content.replace('[NAME]', name)
            content = content.replace('[SENDER_NAME]', your_name)

            # set up SMTP connection
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email,
                                    msg=f"Subject:Happy Birthday!\n\n{content}.")




