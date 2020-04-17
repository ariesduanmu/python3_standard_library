# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 09:22:14
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 09:24:44
# 10.4.9 Subclassing Process

import multiprocessing

class Worker(multiprocessing.Process):
    def run(self):
        print(f'In {self.name}')
        return

if __name__ == '__main__':
    jobs = []
    for _ in range(5):
        p = Worker()
        jobs.append(p)
        p.start()

    for j in jobs:
        j.join()