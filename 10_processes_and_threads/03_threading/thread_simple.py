# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-11 17:17:52
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 14:01:32
# 10.3.1 Thread Objects

import threading
import time

def worker(num):
    print(f'Worker: {num}')
    time.sleep(1)
    print(f'Worker {num} Done')

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()