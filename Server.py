from scapy.all import *
import arp_spoofing

arp_check = arp_spoofing.ARP_Spoofing()

def Server():
	Run_Scan_Insert()

def Detection(p):
	if (ARP in p) and (p[ARP].op == 2):
		arp_check.check(p)
		
def Run_Scan_Insert():
	print "Starting to sniff network fraffic..."
		
	while True:
		packet = sniff(count = 1, prn = Detection)
