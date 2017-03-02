from scapy.all import *


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
    head = None
    tail = None

    def __init__(self):
        self.head = None


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


class synFlood(object):
    def __init__(self):
        self.dic = {}
	
    def synFloodIdentify(self, tuple):
        # checks for syn flood attack
        # input: arrey containing packets and time
        # output: if there is synflood attack, return the ip of the 'bad guy'
		
        linklistlen = 0
        pack = tuple[0]
        
        t = tuple[1]  # nice time
	
	if tuple[0][TCP]:
		print "TCP"
		
		ip = pack[TCP][0]	
		
		if tuple[0][TCP][0].flags & 0x02:
			print "SYN"
			
			if ip not in self.dic:
			    self.dic[ip] = SingleList()  # Generates a new link list
			# append
			self.dic[ip].append(t)  # add to the link list dic[ip] another time
			curr = self.dic[ip].head
						
			if len(self.dic) != 0:  # if dic(contain syn packet) arnt empty		
				# erase
				while curr != None:
					if buildtime(curr.data) - buildtime(self.dic[ip].head.data) > 1000000:
					# if the difference between the first node and the current node big than 1 second
						self.dic[ip] = self.dic[ip].next
						curr = self.dic[ip].head
					curr = curr.next
						

			# identify
			curr = self.dic[ip].head
			linklistlen = 0
			while curr != None:
				print linklistlen
				linklistlen += 1
				curr = curr.next
			if linklistlen >= 60:
				return "syn flood in ip ", ip 
        return None
