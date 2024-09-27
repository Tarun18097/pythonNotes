# wap that takes email addresses from user and messages from user and using smtp library,send message to email addresses
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv() # load environment variables from .env file

Passwd = os.getenv("EMAIL_PASSWORD") # getting app password for email


def make_list_of_email_add():
    list_of_emails = []
    print("To stop the loop, enter 'stop'")
    while True:
        email = input("Enter email: ")
        if email.lower() == 'stop':
            break
        else:
            list_of_emails.append(email)
    return list_of_emails

# Collecting message and list of emails
user_msg = input("Enter your message: ")
list_of_emails = make_list_of_email_add()

# SMTP server setup
SERVER = "smtp.gmail.com"
PORT = 587  # Gmail SMTP server port for TLS
FROM = "tarunkukreti789@gmail.com"
PASSWORD = Passwd

# Crafting the email message

SUBJECT = "automated message"  # You can change this to customize the subject
TEXT = user_msg

message = MIMEMultipart() # creating the email message
message['From'] = FROM   # sender's email
message['To'] = ", ".join(list_of_emails) 
message['Subject'] = SUBJECT # subject of the email

# Attach the message text
message.attach(MIMEText(TEXT, 'plain'))

# Sending the email
try:
    server = smtplib.SMTP(SERVER, PORT)
    server.starttls()  # Start TLS for security
    server.login(FROM, PASSWORD)
    server.sendmail(FROM, list_of_emails, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
finally:
    server.quit()