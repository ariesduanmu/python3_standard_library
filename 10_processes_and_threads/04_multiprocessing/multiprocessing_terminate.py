# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-15 14:27:52
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 14:30:49
# 10.4.6 Terminating Processes

import multiprocessing
import time

def slow_worker():
    print('Starting worker')
    time.sleep(0.1)
    print('Finished worker')

if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    print(f'BEFORE: {p} {p.is_alive()}')

    p.start()
    print(f'DURING: {p} {p.is_alive()}')

    p.terminate()
    print(f'TERMINATED: {p} {p.is_alive()}')

    p.join()
    print(f'JOINED: {p} {p.is_alive()}')