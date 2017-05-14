
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print 'Script demonstrates How To send emails using Python'
print '==================================================='
print ''

yLogin = "xxx@talktalk.net"
yPassword = "xxx"

server = smtplib.SMTP('smtp.talktalk.net', 587) #smtp,port number
server.ehlo()
server.starttls()
server.ehlo()

server.login (yLogin, yPassword)

fromaddr = "xxx@talktalk.net"
toaddr = "xxx@talktalk.net"
subject = "From Python"


msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject

body = "Sent from Python"

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

print 'message sent'
