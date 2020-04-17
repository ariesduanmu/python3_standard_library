# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 11:56:58
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 14:18:57
# 10.4.15 Managing Shared State

import multiprocessing
from pprint import pprint

def worker(d, key, value):
    d[key] = value

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [
        multiprocessing.Process(
            target=worker,
            args=(d, i, i*2)
            )
        for i in range(10)
    ]

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    pprint(f'Results: {d}')