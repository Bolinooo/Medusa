from medusa.Message import Message
from medusa.SmtpHandler import connect_smtp


def sent_mail(amount, sender, pwd, recipient, subject, body=""):
    """
    Function to sent a single mail
    """

    count = 0
    while count < amount:

        mail = Message(sender, recipient, subject, body)
        server = connect_smtp()
        server.login(sender, pwd)
        text = mail.msg.as_string()
        try:
            server.sendmail(mail.msg['From'], mail.msg['recipient'], text)
        except KeyboardInterrupt:
            print("You're kind enough to stop suffering.")
            break
        count += 1
