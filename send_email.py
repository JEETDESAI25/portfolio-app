import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

#add your email address
    username = ''
    password = os.getenv("PASSWORD")

#add your email address
    reciever = ""
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)




