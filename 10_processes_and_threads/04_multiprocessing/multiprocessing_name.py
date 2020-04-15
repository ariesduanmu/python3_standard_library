# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-15 13:45:07
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 14:03:18
# 10.4.3 Determining the Current Process

import multiprocessing
import time

def worker():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(2)
    print(name, 'Exiting')

def my_service():
    name = multiprocessing.current_process().name
    print(name, 'Starting')
    time.sleep(3)
    print(name, 'Exiting')

if __name__ == '__main__':
    service = multiprocessing.Process(
        name='my_service',
        target=my_service,
        )
    worker_1 = multiprocessing.Process(
        name='worker 1',
        target=worker,
        )
    worker_2 = multiprocessing.Process(
        target=worker,
        )

    # 居然是顺序执行的
    worker_1.start()
    worker_2.start()
    service.start()