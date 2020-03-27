import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #os.path
from email.mime.multipart import MIMEMultipart

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "Antoine Flynn"
email["to"] = "aflynneastwood@gmail.com"
email["subject"] = "Enlarge your bag"

email.set_content(html.substitute({"name" : "Antoine"}), "html")

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login("aflynneastwood@gmail.com", "645Tit0inE")
	smtp.send_message(email)
	print("Sent successfully!")

