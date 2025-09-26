from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from string import Template
from pathlib import Path
import smtplib
import csv


message = MIMEMultipart()
message["from"] = "Khadija Khatun"
message["to"] = "khatukhadija556@gmail.com"
message["subject"] = "This is subject"
message.attach(MIMEText("Body text More"))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()               
    smtp.starttls()            
    smtp.login("khadija.codencoit@gmail.com", "erws ccfb gzwh nhip")   
    smtp.send_message(message)  
    print("Sent....go")