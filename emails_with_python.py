# see https://en.wikibooks.org/wiki/Python_Programming/Email for more gmail stuff
# see https://docs.python.org/3.4/library/email-examples.html for specific python commands

# Import smtplib for the actual sending function (simple message transfer protocal library)
import smtplib

# Import the email modules we'll need for creating Multipurpose Internet Mail Extensions messages
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# setting email to send from
gmail_login = "your gmail username"

# initialize message
msg = MIMEMultipart()
msg['From'] = gmail_login + "@gmail.com"
msg['To'] = "fake_receiver@gmail.com"
msg['Subject'] = 'Send plots'

# message body
body = "Python test mail"
msg.attach(MIMEText(body))

# attaching image
img = MIMEImage(open('test.png', 'rb').read())
msg.attach(img)

# The first argument is the server's hostname, the second is the port. The port used varies depending on the server.
s = smtplib.SMTP('smtp.gmail.com', 587)

# set up the proper connection for sending mail.
# may not be necessary depending on the server you connect to. ehlo() is used for ESMTP servers
# for non-ESMTP servers, use helo() instead. See Wikipedia's article about the SMTP protocol for more information about this.
# The starttls() function starts Transport Layer Security mode, which is required by Gmail.
s.ehlo()
s.starttls()
s.ehlo()

# login
s.login(gmail_login, "put password here")

# send message
s.send_message(msg)

# quit the server
s.quit()

# for batch file notification
print("email sent")
