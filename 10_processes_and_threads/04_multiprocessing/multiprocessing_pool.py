# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 14:33:25
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 14:47:02
# 10.4.17 Process Pools

# By default, Pool creates a fixed number of worker processes and 
# passes jobs to them until there are no more jobs.
# Setting the maxtasksperchild parameter tells the pool to restart
# a worker process after it has finished a few tasks, preventing long-running workers from
# consuming ever more system resources.

import multiprocessing

def do_calculation(data):
    return data * 2

def start_process():
    print(f'Starting {multiprocessing.current_process().name}')

if __name__ == '__main__':
    inputs = list(range(100))
    # print(f'Input : {inputs}')

    # builtin_outputs = list(map(do_calculation, inputs))
    # print(f'Built-in: {builtin_outputs}')

    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
        maxtasksperchild=4
    )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close()
    pool.join()

    # print(f'Pool : {pool_outputs}')