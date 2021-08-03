from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from os import name
from pathlib import Path
from string import Template

import smtplib

template = Template(Path("template.html").read_text())

message = MIMEMultipart()
message["from"] = "Raunak Mandal"
message["to"] = "<receiver_email>"
message["subject"] = "Hello"
body = template.substitute({"name": "Raunak Mandal"})
body = template.substitute(name="Raunak Mandal")
message.attach(MIMEText(body, "html"))

with smtplib.SMTP(host="<your_host>", port="<your_port>") as mail:
    mail.ehlo()
    mail.starttls()  # uses as transport layer security (TLS)
    mail.login("<your_email>", "<your_password>")
    mail.send_message(message)
    print("Sent...")
