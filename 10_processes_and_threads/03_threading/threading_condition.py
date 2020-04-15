# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-13 09:33:19
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 13:55:42
# 10.3.9 Synchronizing Threads

import logging
import threading
import time

def consumer(cond):
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is available to consumer')

def producer(cond):
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
    )

condition = threading.Condition()
c1 = threading.Thread(name='c1', 
                      target=consumer,
                      args=(condition,))

c2 = threading.Thread(name='c2', 
                      target=consumer,
                      args=(condition,))

p = threading.Thread(name='p', 
                     target=producer,
                     args=(condition,))

c1.start()
time.sleep(0.2)
c2.start()
time.sleep(0.2)
p.start()