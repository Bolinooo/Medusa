from email.mime.multipart import MIMEMultipart


class Message(object):
    """
    Object for single mail with it's corresponding attributes
    """

    def __init__(self, sender, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        self.body = body
        self.msg = msg
