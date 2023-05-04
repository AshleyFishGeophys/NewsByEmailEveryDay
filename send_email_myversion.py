import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Use env for more secure password storage!
def send_email(title, content):
    host = "smtp.gmail.com"
    port = 465

    username = "ashleymfish@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "ashleymfish@gmail.com"
    context = ssl.create_default_context()

    message = MIMEMultipart()
    message['From'] = username
    message['To'] = receiver
    message['Subject'] = title

    message.attach(MIMEText(content, 'plain'))

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.as_string())

