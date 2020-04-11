# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-11 17:33:40
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-11 17:43:04
import threading
import time
import logging

def daemon():
    logging.debug('Starting')
    time.sleep(0.2)
    logging.debug('Exiting')

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
    )

d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()