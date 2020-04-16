#!/usr/bin/env python3

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

sender_email = input('What email would you like to send from?')
password = input("Type your password and press enter: ")

receiver_email = input('What email would you like to send to?')


message1 = input('Please write your subject line:')
message2 = input('Please write your message:')

message = """\
Subject: {subj}

{mes}""".format(subj=message1, mes = message2)



context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
