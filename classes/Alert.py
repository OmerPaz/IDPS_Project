import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Alert(object):
	
	def __init__(self):
		self._srcAddr = 'cyberproject11@gmail.com' # src address
		self._dstAddr = 'cyberproject11@gmail.com' # dst address
		self._password = '!CyberProject11' # password for the src address

	def send(self, subject, message):
		self._msg = MIMEMultipart()
		self._msg['From'] = self._srcAddr
		self._msg['To'] = self._dstAddr
		self._msg['Subject'] = subject
		 
		self._msg.attach(MIMEText(message, 'plain'))
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(self._srcAddr, self._password)
		text = self._msg.as_string()
		server.sendmail(self._srcAddr, self._dstAddr, text)
		server.quit()
		