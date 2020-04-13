# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-13 10:57:41
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-13 11:00:13
import threading
import logging

def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')

def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquried directly')
    finally:
        lock.release()

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock, ))
nw = threading.Thread(target=worker_no_with, args=(lock, ))

w.start()
nw.start()