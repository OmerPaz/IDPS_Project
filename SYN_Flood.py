import thread
from time import gmtime, strftime
from db.py import *
class synFlood(object):
	

	def __init__(self):
		self.dic={}
	def addSec(timeSTR):
		sec=int(timeSTR[6:8])
		if sec==60:
			sec=0
			min=int(timeSTR[3:5])
			if min==60:
				min=0
				hr=int(timeSTR[:2])
				if hr==24:
					hr=0
				else:
					hr++
			else:
				min++
		else:
			sec++
		str="%d:%d:%d" %(hr,min,sec)
		return str
	def synFlood(self,arr):
		#checks for syn flood attack in the database
		#input: arrey containing lines in the db wich
		count=0
		for i in arr:
			if arr[i][1]==6:#the flag repretance the syn packet
				if arr[i][2] in self.dic:
					arr[i][2]++
				else
					arr[i][2]=1
		for i in dic:
			if dic[i][2]==60
				return "syn flood in ip ",dic[i][2]
			else
				del dic[i][2]
		
	return NULL




