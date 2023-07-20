import smtplib
import datetime as dt
import random

MY_EMAIL = "bhosalerutul117@gmail.com"
MY_PASSWORD = "lbltklyihkeaihfe"
a1=1
now = dt.datetime.now()
weekday = now.weekday()
print(a1)
if weekday == 2:
    print(a1+1)
    with open("quotes.txt") as  quote_file:
        all_quotes = quote_file.readlines()
        quotes = random.choice(all_quotes)
        print(quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        print(a1+2)
        connection.starttls()
        connection.login(MY_EMAIL , MY_PASSWORD)
        connection.sendmail( from_addr=MY_EMAIL,
                             to_addrs=MY_EMAIL,
                             msg=f"Subject:Monday motivation\n\n{quotes}")
    print(a1+3)

print(a1+4)