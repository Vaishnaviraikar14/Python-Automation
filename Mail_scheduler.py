import os
import time
import psutil
import urllib.request
import smtplib
import schedule
from sys import *
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import socket
from urllib.error import URLError
import datetime as dt 

def is_connected():
    try:
        urllib.request.urlopen('http://www.google.com', timeout=1)
        return True
    except (URLError, socket.timeout):
        return False

def Mail_Sender():
    print("Mail_Sender function is running...")
    try:
        fromaddr = "vaishnaviraikar1403@gmail.com"
        toaddr = "vaishnaviraikar1403@gmail.com"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr

        body = """
        Hello,
        Wishing you a day filled with happiness and a year filled with joy. Happy birthday!”
        
        Thanks & Regards,
        Vaishnavi Raikar 
        """

        Subject = """
        Mail scheduler for b'day wish
        """

        msg['Subject'] = Subject

        msg.attach(MIMEText(body,'plain'))
        

        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()

        s.login(fromaddr,"hkfq iedc nhyq hhwu")
        text = msg.as_string()

        s.sendmail(fromaddr,toaddr,text)
        s.quit()

        send_time = dt.datetime(2023,10,24,18,50,0)
        current_time = dt.datetime.now()

        print("send_time:", send_time)  # Debug line
        #print("current_time:", current_time)  # Debug line

    except Exception as E:
        print("Unable to send mail.",E)

def main():
    schedule.every().day.at("18:50").do(Mail_Sender)

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
