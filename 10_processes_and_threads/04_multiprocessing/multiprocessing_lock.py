# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 10:53:58
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 11:13:58
# 10.4.12 Controlling Access to Resources

# not work for windows
import multiprocessing
import sys

def worker_with(lock, stream):
    with lock:
        stream.write('Lock acquired via with\n')

def worker_no_with(lock, stream):
    lock.acquire()
    try:
        stream.write('Lock acquired directly\n')
    finally:
        lock.release()

lock = multiprocessing.Lock()
w = multiprocessing.Process(
    target=worker_with,
    args=(lock, sys.stdout),
    )

nw = multiprocessing.Process(
    target=worker_no_with,
    args=(lock, sys.stdout),
    )

w.start()
nw.start()

w.join()
nw.join()

