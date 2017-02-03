import thread
from time import gmtime, strftime


def main():
	s1=Scan_Insert()
	s1.ScanForTest(1)
	d1=Detection()
	d1.packets=s1.listForTest	
	d1.Check()

if __name__ == "__main__":
    main()


class Scan_Insert(object):
	
	def __init__(self, interface):
		self.listForTest=[()]
		self.d=Detection()
		_interface = interafce

	def ScanForTest(self,num):
		for i in num:
			sniff(iface = this._interface, prn = InsertForTest)


	def Scan(self):
		while True:
			sniff(iface = this._interface, prn = Insert)
	def InsertForTest(self, packet):
		time=datetime.now().strftime('%H:%M:%S')
		self.listForTest+=(packet,time)



	def Insert(self, packet):
		time=datetime.now().strftime('%H:%M:%S')
		self.d.buildList(packet,time)

		print "New Packet"

class Detection(object):
	
	def __init__(self):
		self.sf=synFlood()
		self.packets=[()]
		a=Check(self)
		if a!=None:
			print "%s" %a 
	
	def buildList(packet,time):
		self.packets+=(packet,time)


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
					hr+=1
			else:
				min+=1
		else:
			sec+=1
		str="%d:%d:%d" %(hr,min,sec)
		return str
		
	def Check(self):
		# Checks for attack in the database
		# Calls for other functions in Dectection, every function checks other attack
		id=1		
		while i in packets:
				
			if datetime.now().strftime('%H:%M:%S')==addSec(timeEnd):		
				
				ret=sf.synFloodIdentify(packets)
				if ret!=None:
					return ret
				time=addSec(time)
				id+=1
				timeEnd=datetime.now().strftime('%H:%M:%S')
		return None

class synFlood(object):
	

	def __init__(self):
		self.dic={}


	def synFloodIdentify(self,arr):
		#checks for syn flood attack in the database
		#input: arrey containing lines in the db wich
		count=0
		for i in arr:
			if SYN in arr[i][0]:
				if arr[i][0].ip in self.dic:
					dic[ arr[i][0].ip ][2]+=1
				else:
					dic[ arr[i][0].ip ][2]=1
		for i in dic:
			if dic[i][2]==60:
				return "syn flood in ip ",dic[i][2]
			else:
				del dic[i][2]
		
		return None




