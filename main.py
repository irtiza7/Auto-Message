"""
Idea: The application sends a message on WhatsApp.
"""
from datetime import date
import time
import pywhatkit as pywt

contact = "+923090047457"  # input("Enter the contact: ")
message = "Automatic Message."  # input("Enter the message: ")
tragetted_hour = int(input("Enter hour (in 24-hour format): "))
tragetted_minutes = int(input("Enter minutes: "))
targetted_date = int(input("Enter date (01 to 31): "))
wait_sec = int(input("After how many seconds (15 to onwards) to send the message: "))

while True:
    today_date = date.today()
    if targetted_date == int(today_date.strftime("%d")):
        break

    time.sleep(1)

pywt.sendwhatmsg(contact, message, tragetted_hour, tragetted_minutes, wait_sec)
