import threading
import logging

class MyThread(threading.Thread):
	def __init__(self, group=None, target=None, name=None,
		         args=(), kwargs=None, *, daemon=None):
		super().__init__(group=group, target=target, name=name,
			daemon=daemon)
		self.args = args
		self.kwargs = kwargs

	def run(self):
		logging.debug(f'running with {self.args} and {self.kwargs}')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
    )

for i in range(5):
	t = MyThread(args=(i,), kwargs={'a':'A', 'b':'B'})
	t.start()