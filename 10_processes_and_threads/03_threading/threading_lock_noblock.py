# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-13 10:23:20
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 13:55:17
# 10.3.8 Controlling Access to Resources

import logging
import threading
import time

def lock_holder(lock):
    logging.debug(f'{time.ctime()}: Starting')
    while True:
        lock.acquire()
        try:
            logging.debug(f'{time.ctime()}: Holding')
            time.sleep(2)
        finally:
            logging.debug(f'{time.ctime()}: Not holding')
            lock.release()
        time.sleep(2)

def worker(lock):
    logging.debug(f'{time.ctime()}: Starting')
    num_tries = 0
    num_acquires = 0
    while num_acquires < 3:
        time.sleep(1)
        logging.debug(f'{time.ctime()}: Trying to acquire')
        have_it = lock.acquire(0)
        try:
            num_tries += 1
            if have_it:
                logging.debug(f'{time.ctime()}: Iteration {num_tries}: Acquired')
                num_acquires += 1
            else:
                logging.debug(f'{time.ctime()}: Iteration {num_tries}: Not acquired')
        finally:
            if have_it:
                lock.release()
    logging.debug(f'{time.ctime()}: Done after {num_tries} iterations')

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )

lock = threading.Lock()

holder = threading.Thread(
    target=lock_holder,
    args=(lock,),
    name='LockHolder',
    daemon=True,
    )
holder.start()

worker = threading.Thread(
    target=worker,
    args=(lock,),
    name='Worker',
    )
worker.start()