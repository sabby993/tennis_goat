from email.mime.text import MIMEText
import smtplib


def send_email(email, response, percentage_goat, count_total):
    from_email="roysabby1993@gmail.com"
    from_password="Madman@007"
    to_email=email

    subject="Tennis G.O.A.T"
    message="Hey there your selected G.O.A.T is <strong>%s</strong>. <br> Percentage of people who think %s is the G.O.A.T is %s percent out of %s people." % (response,response,percentage_goat, count_total)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
