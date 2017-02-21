import thread
from time import gmtime, strftime
from db.py import *
class Detection(object):
	
	def __init__(self):
		
		a=Check(self)
		if a!=NULL:
			print "%s" %a 
					
	
	def Check(self):
		# Checks for attack in the database
		# Calls for other functions in Dectection, every function checks other attack
		id=1		
		while ReadDB(self,id=id+1))!=NULL:
			timeStart=datetime.now().strftime('%H:%M:%S')	
			if datetime.now().strftime('%H:%M:%S')==addSec(timeEnd):		
				
				a=ReadDB(self,time=time)
				ret=synFlood(a)
				if synFlood(a)!=NULL:
					return ret
				time=addSec(time)
				id++
				timeEnd=datetime.now().strftime('%H:%M:%S')
		return NULL
