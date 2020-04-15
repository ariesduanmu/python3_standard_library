# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-15 13:37:25
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 13:58:02
# 10.4.2 Importable Target Functions

import multiprocessing
import multiprocessing_import_worker

if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=multiprocessing_import_worker.worker, args=(i,))
        jobs.append(p)
        p.start()