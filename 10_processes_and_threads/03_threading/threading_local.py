import random
import threading
import logging

class CustomData():
	def setvalue(self, value):
		self.value = value

class MyLocal(threading.local):
	def __init__(self, value):
		super().__init__()
		logging.debug(f'Initializing {self}')
		self.value = value

def show_value(data):
	try:
		val = data.value
	except AttributeError:
		logging.debug('No value yet')
	else:
		logging.debug(f'value={val}')

def worker(data):
	show_value(data)
	data.value = random.randint(1,100)
	show_value(data)

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )

local_data = MyLocal(1000)
show_value(local_data)


not_local_data = CustomData()
show_value(not_local_data)
not_local_data.setvalue(999)
show_value(not_local_data)


for i in range(2):
	t = threading.Thread(target=worker, args=(local_data,))
	t.start()

for i in range(2):
	t = threading.Thread(target=worker, args=(not_local_data,))
	t.start()