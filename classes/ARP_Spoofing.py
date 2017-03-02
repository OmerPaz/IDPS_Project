from scapy.all import *
import datetime
import pcapy
import time
import Alert

class ARP_Spoofing(object):
	
	def __init__(self):
		self.arp_table = {}
		self._alert = Alert.Alert()

	def check(self, packet):
		self.packet = packet
		self.ip_addr = packet[ARP].psrc
		self.mac_addr = packet[ARP].hwsrc
		self._time = time.time()

		self.main_check()

	def main_check(self):
		# main function to check arp spoofing

		self.Check_Time() # Deletes old records

		if (self.Is_Exists()): # Is the packet in the table
			if ((self.Get_Value()) != self.ip_addr): # Is the mac address from the table equals to the given mac address
				self.AlertTo() # If the mac addresses aren't equal, alert
				return

		self.Update_Table() # If the mac addresss doesn't appear in the table, update the table		

	def Update_Table(self):
		# Inserts into the arp_table the ip_addr and mac_addr

		self.arp_table[self.mac_addr] = (self.ip_addr, self._time)

	def Is_Exists(self):
		# Checks if the given ip_addr exists in the arp_table
		# If it exists, it returns True. Otherwise, returns False

		return self.arp_table.has_key(self.mac_addr)

	def Get_Value(self):
		# Returns the mac_addr of the given ip_addr from the arp_table

		return self.arp_table[self.mac_addr][0]

	def Check_Time(self):
		# Deletes old records - If the record is in the ARP table for more than 3min (180sec)

		keys = self.arp_table.keys()

		for key in keys:
			old_time = self.arp_table[key][1]
			if (self._time - old_time) > 180:
				del self.arp_table[key]

	def AlertTo(self):
		# Runs if arp spoofing was found
		"""
		MAC address: self.mac_addr
		First IP address: self.Get_Value()
		Second IP address: self.ip_addr
		"""

		print "ARP Spoofing was found, E-Mail was sent!"

		subject = "Attack Alert: ARP Spoofing was found!"
		message = "ARP conflict was found!\n"
		message += "The MAC address: " + str(self.mac_addr) + " is linked into two IP addresses:\n"
		message += "IP address #1: " + str(self.Get_Value()) + "\n"
		message += "IP address #2: " + str(self.ip_addr) + "\n"
		message += "\n\n" + "Date: " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

		self._alert.send(subject, message)
