from scapy.all import *
#import socket
#import Alert
mip=socket.gethostbyname(socket.gethostname())

def buildtime(time):
    micro = time.microsecond
    sec = time.second
    minn = time.minute
    hour = time.hour
    btime = micro + (sec * 1000000) + (minn * 1000000 * 60) + (hour * 1000000 * 60 * 60)  # milion microsecond= 1 sec
    return btime

class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next

class SingleList(object):

    def __init__(self):
        self.head = None
	self.tail = None

    def show(self):
        print "Showing list data:"
        current_node = self.head
        while current_node is not None:
            print current_node.data, " -> ",
            current_node = current_node.next
        print None


    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node


    def remove(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
                # if this is the first node (head)
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next


class pingFlood(object):
    def __init__(self):
        self.dic = {}
	#*************	
	self.seconds=10*1000000
	self.pktnum=3
	#*************	
	#self._alert = Alert.Alert()
    
    def get_ip_address(a):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    def pingOfDeath(self,pkt):
        if pkt[0][ICMP]:
	    if len(pkt[0])>500:
		print "ping of death"
	

    def pingFloodIdentify(self, pkt):
        
        # input: arrey containing packet and time
        # output: if there is ping flood attack, print the ip of the 'bad guy'
        linklistlen = 0
        t = pkt[1]  # nice time
	if pkt[0][ICMP]:
		ip = pkt[0][0].getlayer(IP).src#ip of the pkt sorce
		if (pkt[0][ICMP][0].code is 0) and (pkt[0][0].getlayer(IP).dst == self.get_ip_address()):
			#if the packet is ping and if the destination is me(we dont want to get pack that was sended 				 from our computer)
			if ip not in self.dic:
			    self.dic[ip] = SingleList()  # Generates a new link list	 
			# append 
			self.dic[ip].append(t)  # add to the link list dic[ip] another time
			curr = self.dic[ip].head
			print curr.data			
			if len(self.dic) != 0:  # if dic(contain ICMP packet) arnt empty		
				# *********erase
				while curr != None:
					if buildtime(curr.data) - buildtime(self.dic[ip].head.data) > self.seconds:
						# if the difference between the first node and the current node big 							  than 1 second
						self.dic[ip].head = self.dic[ip].head.next
						curr = self.dic[ip].head
					curr = curr.next
						

			# identify
			curr = self.dic[ip].head
			linklistlen = 0	
			while curr != None:
				linklistlen += 1
				print linklistlen
				curr = curr.next
			
			if linklistlen >= self.pktnum:
				print "ping flood in ip ", pkt[0][0].getlayer(IP).dst
				#subject = "Attack Alert: ping flooding was found!\n"
				#message = "ping flood in ip ", pkt[0][0].getlayer(IP).dst
				#self._alert.send(subject, message)  
        
