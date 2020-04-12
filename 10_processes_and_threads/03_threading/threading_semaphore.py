import logging
import random
import threading
import time

class ActivePool:
	def __init__(self):
		super(ActivePool, self).__init__()
		self.active = []
		self.lock = threading.Lock()

	def makeActive(self, name):
		with self.lock:
			self.active.append(name)
			logging.debug