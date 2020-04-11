# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-11 17:17:52
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-11 17:19:29
import threading

def worker(num):
    print(f'Worker: {num}')

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()