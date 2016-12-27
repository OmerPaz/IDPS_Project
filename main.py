from scapy.all import *
import datetime
import pcapy
import time
import thread
import Server

def main():
	print "The available interfaces are:"
	for dev in pcapy.findalldevs():
		print dev

	print "Enter the name of the interface to sniff: "
	interface = raw_input()

	Server mainServer = Server(interface)


if __name__ == "__main__":
	main()
	