# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-13 10:07:45
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-13 10:18:18
import logging
import random
import threading
import time

class Counter:
    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug(f'Waiting for lock: {self.value}')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value+1
        finally:
            logging.debug(f'Release lock: {self.value}')
            self.lock.release()

def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug(f'Sleeping {pause:.2f}')
        time.sleep(pause)
        c.increment()
    logging.debug('Done')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug(f'Counter: {counter.value}')