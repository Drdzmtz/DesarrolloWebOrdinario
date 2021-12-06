import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import EMAILADDRESS, EMAILPASSWORD


class Mail_Sender():

    def __init__(self, **kwargs):

        self.addresses_to_send  =   kwargs.get("receivers", [])
        self.subject            =   kwargs.get("subject", "")
        self.html_template      =   kwargs.get("html_template", "")
        self.text_template      =   kwargs.get("text_template", "")

        self.sender_address     =   EMAILADDRESS
        self.sender_password    =   EMAILPASSWORD

    def send_mail(self):

        message = MIMEMultipart("alternative")
        message["Subject"] = self.subject
        message["From"] = self.sender_address
        message["To"] = ", ".join(self.addresses_to_send)

        part1 = MIMEText(self.text_template, "plain")
        part2 = MIMEText(self.html_template, "html")

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_address, self.sender_password)

            server.sendmail(
                self.sender_address, self.addresses_to_send, message.as_string()
            )