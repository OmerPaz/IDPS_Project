import thread
import Scan_Insert

class Server(object):
	
	def __init__(self, interface):
		_interface = interface
		_scan_insert = Scan_Insert(_interface)
		_detect = Detect()

	def scan_insert(self):
		thread.start_new_thread(_scan_insert.Scan, ())

	def detect(self):
		thread.start_new_thread(_detect.check, ())
