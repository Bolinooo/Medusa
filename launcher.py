#!/usr/bin/env python

from medusa.Bomber import sent_mail
from medusa.Checker import get_amount

__author__ = "Bolinooo"


def main():

    number = get_amount()

    sender = str("Fill in sender")
    pwd = str("Fill in pwd")
    recipient = str("Fill in recipient")
    subject = str("Fill in subject")
    body = str("Fill in body")

    sent_mail(number, sender, pwd, recipient, subject, body)

if __name__ == "__main__":
    main()
