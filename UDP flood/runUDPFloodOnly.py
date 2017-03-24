from scapy.all import *
import udpflood
from datetime import datetime

c = udpflood.UDPFlood()

while True:
	a = sniff(count = 1)
	b = datetime.now()
	p = (a, b)
	c.UDPFloodIdentify(p)
	
