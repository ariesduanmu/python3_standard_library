# 10.3.4 Enumerating All Threads

import random
import threading
import time
import logging

def worker(pause):
	# pause=random.randint(1,5)/10
	logging.debug(f'sleep {pause:.2f}')
	time.sleep(pause)
	logging.debug('ending')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
    )

for i in range(3):
	t = threading.Thread(target=worker, args=((i+1)/10,), daemon=True)
	t.start()

main_thread = threading.main_thread()

for t in threading.enumerate():
	if t is main_thread:
		continue
	logging.debug(f'joining {t.getName()}')
	t.join()