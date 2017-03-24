from scapy.all import *
import pingFlood
from datetime import datetime

c = pingFlood.pingFlood()

while True:
	a = sniff(count = 1)
	b = datetime.now()

	p = (a, b)
	c.pingFloodIdentify(p)
	
	#if k!=None:	
	#	print k
