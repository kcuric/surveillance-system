import cv2
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

class EmailSender(object):

    def __init__(self, camera_num, img_data):
        self.data = img_data
        self.camera_num = camera_num

    def send_email(self, receiver_mail):
        now = datetime.now()
        filename = now.strftime("%Y-%m-%d---%H-%M-%S") + ".jpg"
        path = '/tmp/' + filename
        sender = "sissurvailance@gmail.com"
        receiver = receiver_mail
        nparr = np.fromstring(self.data, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        cv2.imwrite(path, img_np)

        date_and_time = now.strftime("%d.%m.%Y. %H:%M:%S")

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "Face detected"
        body = f"At {date_and_time}, camera #{self.camera_num} detected a face. Find attached image with the detected face."
        msg.attach(MIMEText(body, 'plain'))

        attachment = open(path, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)

        username = "sissurvailance@gmail.com"
        password = "fw#22xCz"

        try:
            smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(username, password)
            text = msg.as_string()
            smtpObj.sendmail(sender, receiver, text)
            smtpObj.quit()
            print(f"Email sent to {receiver}.")
        except Exception as e:
            print("Unable to send the email.")
