#! /usr/bin/env python3

import smtplib
import os

def send_email():
    body = os.environ.get('CONTEST_BODY')
    gmail_user = os.environ.get('MAIL_USERNAME')
    gmail_password = os.environ.get('MAIL_PASSWORD')
    subject = os.environ.get('CONTEST_SUBJECT')
    to = os.environ.get('CONTEST_RECIP')
    message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (gmail_user, to, subject, body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, gmail_user, message)
        server.close()
    except:
        print("Failed to send mail")

        
if __name__ == '__main__':
    send_email()