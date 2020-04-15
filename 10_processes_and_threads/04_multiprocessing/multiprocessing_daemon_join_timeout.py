# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-15 14:07:13
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-15 14:24:27
# 10.4.4 Daemon Processes
# 10.4.5 Waiting for Processes

import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process()
    print(f'Starting: {p.name} {p.pid}')
    sys.stdout.flush()
    time.sleep(2)
    print(f'Exiting: {p.name} {p.pid}')
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print(f'Starting: {p.name} {p.pid}')
    sys.stdout.flush()
    print(f'Exiting: {p.name} {p.pid}')
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(
        name='daemon',
        target=daemon,
        )
    d.daemon = True

    n = multiprocessing.Process(
        name='non_daemon',
        target=non_daemon,
        )
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()

    d.join(1)
    print(f'd.is_alive() {d.is_alive()}')
    n.join()