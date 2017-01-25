from scapy.all import *
import datetime
import pcapy
import time
import thread
import sqlite3

class Database(object):

	def __init__(self):
		self.conn=sqlite3.connect('db.db')
		print "Database created and opened succesfully"
		c = self.conn.cursor()
		#PROTOCOL=the protocol that the packet was sended
		#SRC_IP=the ip of the sorce 
		#DST_IP=the ip of the destination
		#SRC_MAC=the mac of the sorce 
		#DST_MAC=the mac of the destination
		#TTIME=the time that the packet was arrived
		c.execute('''CREATE TABLE par (
			ID                 INT       NOT NULL AUTO_INCREMENT,
			PROTOCOL           TEXT,
			SRC_IP             TEXT,
			DST_IP             TEXT,
			SRC_MAC            TEXT,
			DST_MAC            TEXT,
			SRC_PORT           INT,
			DST_PORT           INT,
			TTIME              TEXT      NOT NULL
			)''')
		self.conn.commit()


	def WriteLog(self, packet):
		# Gets a packet, and inserts every part of the packet (Source IP, Dest ip...) to the correct table
		count=1
		time=datetime.datetime.now().strftime("%H:%M:%S") + ": " + str(len(packet))
		protocol=NULL
		SRC_IP=packet[IP].src
		DST_IP=packet[IP].dst
		#support just tcp and udp
		if TCP in packet:
			protocol="TCP"
			SRC_PORT=str(packet[TCP].sport)
			DST_PORT=str(packet[TCP].dport)
		elif UDP in packet:
			protocol="UDP"
			SRC_PORT=str(packet[UDP].sport)
			DST_PORT=str(packet[UDP].dport)

		SRC_MAC=packet[Ether].src
		DST_MAC=packet[Ether].dst
		statmt="INSERT INTO par [( ID , PROTOCOL , SRC_IP , DST_IP , SRC_MAC , DST_MAC , SRC_PORT , DST_PORT , TTIME)] VALUES(%d,%s,%s,%s,%s,%s,%d,%d,%s)" %(count , protocol , SRC_IP , DST_IP , SRC_MAC , DST_MAC , SRC_PORT , DST_PORT , time)
		self.c.execute(statmt)
		self.conn.commit()
	
	def ReadDB(self,id=None,time=None):
		#the caller : ReadDB(self,id=2)
		#get the all the lines that contain the id or time
		s="";
		if id :
			statmt="SELECT * FROM par WHERE id = '%d'" % id
			for row in self.c.execute(statmt)
				s+=row
		elif time:
			statmt="SELECT * FROM par WHERE id = '%s'" % time
			for row in self.c.execute(statmt)
				s+=row
		return s
			
	def Delete(self, id=None,time=None, TableName):
		# Gets an Id (Int) or time(string) and TableName (String) and removes the packet with the id or time from the correct table in the database
        if id :
			statmt="DELETE * FROM %s WHERE ID LIKE '%s'" %(TableName,id)
			self.conn.execute(statmt)
		elif time:
			statmt="DELETE * FROM %s WHERE TTIME LIKE '%s'" %(TableName,time)
			self.conn.execute(statmt)
        self.conn.commit()

	def Close(self):
		# Closes the Database (Runs only in the end of the program!)
		self.conn.close()



