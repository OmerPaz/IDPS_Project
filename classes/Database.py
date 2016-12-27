import thread

class Database(object):
	
	def __init__(self):
		# Init the database + tables (Only if doesn't exists)

	def WriteLog(self, packet):
		# Gets a packet, and inserts every part of the packet (Source IP, Dest ip...) to the correct table

	def Delete(self, Id, TableName):
		# Gets an Id (Int) and TableName (String) and removes the packet with the id from the correct table in the database

	def Close(self):
		# Closes the Database (Runs only in the end of the program!)
