import smtplib


def connect_smtp():
    """
    Function for setting up correct stmp-server and port
    """
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    return server
