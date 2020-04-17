# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 09:42:44
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 10:21:06
# 10.4.10 Passing Messages to Processes

import multiprocessing

class MyFancyClass:
    def __init__(self, name):
        self.name = name

    def do_something(self):
        proc_name = multiprocessing.current_process().name
        print(f'Doing something fancy in {proc_name} for {self.name}!')

def worker(q):
    obj = q.get()
    obj.do_something()

if __name__ == '__main__':
    queue = multiprocessing.Queue()

    p = multiprocessing.Process(target=worker, args=(queue, ))
    p.start()

    queue.put(MyFancyClass('Fancy Dan'))

    # Indicate that no more data will be put on this queue by the current process. 
    queue.close()
    # Join the background thread. This can only be used after close() has been called. 
    # It blocks until the background thread exits, ensuring that all data in the buffer has been flushed to the pipe.
    queue.join_thread()
    p.join()