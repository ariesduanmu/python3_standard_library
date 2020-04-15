# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-15 13:30:00
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 13:57:32
# 10.4.1 multiprocessing Basics

import multiprocessing

def worker(i):
    print(f'Worker {i}')

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
