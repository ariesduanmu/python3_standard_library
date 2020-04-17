# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 10:46:26
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 10:51:22
# 10.4.11 Signaling Between Process

import multiprocessing
import time

def wait_for_event(e):
    print('wait_for_event starting')
    e.wait()
    print(f'wait_for_event: e.is_set()->{e.is_set()}')

def wait_for_event_timeout(e, t):
    print('wait_for_event_timeout: stating')
    e.wait(t)
    print(f'wait_for_event_timeout: e.is_set()->{e.is_set()}')

if __name__ == '__main__':
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(
        name='block',
        target=wait_for_event,
        args=(e,),
    )
    w1.start()

    w2 = multiprocessing.Process(
        name='nonblock',
        target=wait_for_event_timeout,
        args=(e, 2)
    )
    w2.start()

    print('main: waiting before calling Event.set()')
    time.sleep(3)
    e.set()
    print('main: event is set')