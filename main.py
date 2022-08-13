from datetime import date
import time
import pywhatkit as pywt


contact = input("Enter the contact: ")
message = input("Enter the message: ")
tragetted_hour = int(input("Enter hour (in 24-hour format): "))
tragetted_minutes = int(input("Enter minutes: "))
targetted_date = int(input("Enter date (01 to 31): "))
wait_sec = int(input("After how many seconds (15 to onwards) to send the message: "))

# Pywhatkit doesn't handle dates in its built-in methods, so the following loop extends the application's functionality to handle the date on which the user wants to send the message
while True:
    today_date = date.today()

    # %d extracts the date from the entire data-string returned by today_date
    if targetted_date == int(today_date.strftime("%d")):
        break

    time.sleep(1)

# Parameter 1: Takes a phone number in strint format e.g. +923001234567
# Parameter 2: Takes a messsage in string format
# Parameter 3: Takes an integer between 0 to 23 for specifying the hour
# Parameter 4: Takes an integer between 0 to 59 for specifying the minute
# Parameter 5: Takes an integer, usually 15 or more, which represents the number of seconds to wait before sending the message
pywt.sendwhatmsg(contact, message, tragetted_hour, tragetted_minutes, wait_sec)
