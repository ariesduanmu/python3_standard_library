# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-11 17:20:16
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-11 17:50:21
import threading
import time
import logging

def worker():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')

def my_service():
    logging.debug('Starting')
    time.sleep(1)
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )

t1 = threading.Thread(name='my service', target=my_service, daemon=True)
t2 = threading.Thread(name='worker', target=worker)
t3 = threading.Thread(target=worker)

t2.start()
t3.start()
t1.start()