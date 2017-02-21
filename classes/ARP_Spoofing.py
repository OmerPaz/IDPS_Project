from scapy.all import *
import datetime
import pcapy
import time
import thread

class ARP_Spoofing(object):
	
	def __init__(self):
		# Add: Gets a packet

		this.arp_table = {}
		this.ip_addr = # ip address
		this.mac_addr = # mac address

	def main_check(self):
		# main function to check arp spoofing

		if (Is_Exists()): # Is the packet in the table
			if ((Get_Value()) != this.mac_addr): # Is the mac address from the table equals to the given mac address
				alert() # If the mac addresses aren't equal, alert
		else:
			Update_Table() # If the mac addresss doesn't appear in the table, update the table		

	def Update_Table(self):
		# Inserts into the arp_table the ip_addr and mac_addr

		this.arp_table[this.ip_addr] = this.mac_addr

	def Is_Exists(self):
		# Checks if the given ip_addr exists in the arp_table
		# If it exists, it returns True. Otherwise, returns False

		return this.arp_table.has_key(this.ip_addr)

	def Get_Value(self):
		# Returns the mac_addr of the given ip_addr from the arp_table

		return this.arp_table[this.ip_addr]

	def Alert(self):
		# Works only if arp spoofing was found

		print "ARP Spoofing was found!"
		