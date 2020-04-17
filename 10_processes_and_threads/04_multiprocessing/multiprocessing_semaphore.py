# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 11:26:59
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 11:41:26
# 10.4.14 Controlling Concurrent Access to Resources

# not work on windows
import random
import multiprocessing
import time

class ActivePool:
    def __init__(self):
        super(ActivePool, self).__init__()
        self.mgr = multiprocessing.Manager()
        self.active = self.mgr.list()
        self.lock = multiprocessing.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)

    def __str__(self):
        with self.lock:
            return str(self.active)

def worker(s, pool):
    name = multiprocessing.current_process().name
    with s:
        pool.makeActive(name)
        print(f'Activating {name} now running {pool}')
        time.sleep(random.random())
        pool.makeInactive(name)

if __name__ == '__main__':
    pool = ActivePool()
    s = multiprocessing.Semaphore(3)
    jobs = [
    multiprocessing.Process(
        target=worker,
        name=str(i),
        args=(s, pool)
        )
        for i in range(10)
    ]

    for j in jobs:
        j.start()

    while True:
        alive = 0
        for j in jobs:
            if j.is_alive():
                alive += 1
                j.join(timeout=0.1)
                print(f'Now running {pool}')
        if alive == 0:
            break