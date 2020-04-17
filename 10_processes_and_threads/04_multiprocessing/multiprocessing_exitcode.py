# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 08:54:57
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 09:10:57
# 10.4.7 Process Exit Status

import multiprocessing
import sys
import time

def exit_error():
    sys.exit(1)

def exit_ok():
    return

def return_value():
    return 1

def raises():
    raise RuntimeError('There was an Error!')

def terminated():
    time.sleep(3)

if __name__ == '__main__':
    jobs = []
    funcs = [
        exit_error,
        exit_ok,
        return_value,
        raises,
        terminated,
    ]
    for f in funcs:
        print(f'Starting process for {f.__name__}')
        j = multiprocessing.Process(target=f, name=f.__name__)
        jobs.append(j)
        j.start()

    jobs[-1].terminate()

    for j in jobs:
        j.join()
        print(f'{j.name}.exitcode = {j.exitcode}')
