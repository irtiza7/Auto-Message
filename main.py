import pywhatkit as pywt

# contact = "+923304313760"
contact = input("Enter the contact: ")
message = input("Enter the message: ")
hour = input("Enter the hour: ")
minutes = input("Enter the minutes: ")
day = input("Enter the day: ")
wait_sec = input("After how many seconds to send the message: ")

pywt.sendwhatmsg(contact, message, 19, 12)
