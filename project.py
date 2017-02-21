import thread
import threading
import scapy
from datetime import datetime

pkReady = threading.Event()


def main():
    s1 = Scan_Insert("eth0")
    s1.ScanForTest(1)
    d1 = Detect()
    d1.packets = s1.listForTest
    d1.Check()


if __name__ == "__main__":
    main()


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


class Scan_Insert(object):
    def __init__(self, interface):
        self.listForTest = [()]
        self.d = Detect()
        self._interface = interface

    def Scan(self):
        while True:
            sniff(iface=self._interface, prn=self.Insert)
            pkReady.set()

    def InsertForTest(self, packet):
        time = datetime.now()
        self.listForTest += (packet, time)

    def Insert(self, packet):
        time = datetime.now()
        self.d.buildList(packet, time)
        print "New Packet"


class synFlood(object):
    def __init__(self):
        self.dic = {}

    def buildtime(time):
        micro = time.microsecond
        sec = time.second
        minn = time.minute
        hour = time.hour
        btime = micro + (sec * 1000000) + (minn * 1000000 * 60) + (
        hour * 1000000 * 60 * 60)  # milion microsecond= 1 sec
        return btime

    def synFloodIdentify(self, tuple):
        # checks for syn flood attack
        # input: arrey containing packets and time
        # output: if there is synflood attack, return the ip of the 'bad guy'

        linklistlen = 0
        pack = tuple[0]
        t = tuple[1]  # nice time

        if SYN in tuple[0]:

            if len(dic) != 0:  # if dic(contain syn packet) arnt empty
                # erase
                # for ip in dic:#run on the ip's in dic
                ip = pack.src
                if ip in dic:
                    curr = dic[ip]
                else:
                    dic[ip] = SingleList()  # Generates a new link list
                    curr = dic[ip]
                # append
                dic[pack.src].append(t)  # add to the link list dic[ip] another time

                while curr != 0:
                    if buildtime(curr.data) - buildtime(dic[ip].data) > 1000000:
                        # if the difference between the first node and the current node big than 1 second
                        dic[ip] = dic[ip].next
                        curr = dic[ip]
                    curr = curr.next

                # identify
                curr = dic[ip]
                while curr != 0:
                    linklistlen += 1
                    curr = curr.next
                if linklistlen >= 60:
                    return "syn flood in ip ", ip
        return None


class Detect(object):
    def __init__(self):
        self.sf = synFlood()
        self.packets = [()]

    def buildList(packet, time):
        self.packets += (packet, time)

    def Check(self):
        # Checks for attack in the database
        # Calls for other 	functions in Dectection, every function checks other attack
        while True:
            pkReady.wait()
            for i in packets:
                ret = sf.synFloodIdentify(i)

            pkReady.clear()


