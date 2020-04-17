# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 14:22:16
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 14:32:34
# 10.4.16 Shared Namespaces
import multiprocessing


# Updates to the contents of mutable values in the namespace are not propagated automatically
def producer(ns, event):
    ns.value = 'This is the value'
    ns.my_list.append('This is the list')
    event.set()

def consumer(ns, event):
    print(f'Before event my_list: {ns.my_list}')
    try:
        print(f'Before event value: {ns.value}')
    except Exception as e:
        print(f'Before event value, error:{e}')

    event.wait()
    print(f'After event my_list: {ns.my_list}')
    print(f'After event value: {ns.value}')

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    namespace = mgr.Namespace()
    namespace.my_list = []

    event = multiprocessing.Event()

    p = multiprocessing.Process(
        target=producer,
        args=(namespace, event),
    )
    c = multiprocessing.Process(
        target=consumer,
        args=(namespace, event),
    )

    c.start()
    p.start()

    c.join()
    p.join()