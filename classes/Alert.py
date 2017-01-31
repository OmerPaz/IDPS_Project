import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Alert(object):
	
	def __init__(self):
		this._srcAddr = "cyberproject11@gmail.com"
		this._dstAddr = "cyberproject11@gmail.com"
		this._password = "!CyberProject11"

	def send(self, subject, message):
		this._msg = MIMEMultipart()
		this._msg['From'] = this._srcAddr
		this._msg['To'] = this._dstAddr
		this._msg['Subject'] = subject
		 
		msg.attach(MIMEText(message, 'plain'))
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(fromaddr, this._password)
		text = msg.as_string()
		server.sendmail(this._srcAddr, this._dstAddr, text)
		server.quit()
