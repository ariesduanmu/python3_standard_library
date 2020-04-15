# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-13 09:47:22
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 13:55:52
# 10.3.9 Synchronizing Threads

import threading
import time

def worker(barrier):
    print(f'{threading.current_thread().name} waiting for barrier with {barrier.n_waiting} others')
    try:
        worker_id = barrier.wait()
    except threading.BrokenBarrierError:
        print(f'{threading.current_thread().name} aborting')
    else:
        print(f'{threading.current_thread().name} after barrier {worker_id}')

NUM_THREADS = 3

barrier = threading.Barrier(NUM_THREADS+1)

threads = [
threading.Thread(
    name=f'worker-{i}',
    target=worker,
    args=(barrier,),
    )
    for i in range(NUM_THREADS)
]

for t in threads:
    print(f'{t.name} starting')
    t.start()
    time.sleep(0.1)

barrier.abort()

for t in threads:
    t.join()

