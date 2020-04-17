# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 09:56:31
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 10:44:03
# 10.4.10 Passing Messages to Processes

import multiprocessing
import time

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task.name == 'END':
                print(f'{proc_name}: END Now')
                self.task_queue.task_done()
                break

            if next_task is None:
                print(f'{proc_name}: task is None')
                self.task_queue.task_done()
                break
            print(f'{proc_name}: {next_task}')
            answer = next_task()
            # Indicate that a formerly enqueued task is complete. 
            # Used by queue consumers. 
            # For each get() used to fetch a task, 
            # a subsequent call to task_done() tells the queue that the processing on the task is complete.
            self.task_queue.task_done()
            self.result_queue.put(answer)

class Task:
    def __init__(self, a, b, name='OK'):
        self.a = a
        self.b = b
        self.name = name

    def __call__(self):
        time.sleep(0.1)
        return f'{self.a} * {self.b} = {self.a * self.b}'

    def __str__(self):
        return f'{self.a} * {self.b}'

if __name__ == '__main__':
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()

    print(f'multiprocessing.cpu_count(): {multiprocessing.cpu_count()}')
    num_consumers = multiprocessing.cpu_count() * 2
    print(f'Creating {num_consumers} consumers')
    consumers = [
        Consumer(tasks, results)
        for i in range(num_consumers)
    ]
    for w in consumers:
        w.start()

    num_jobs = 20
    for i in range(num_jobs):
        tasks.put(Task(i, i))

    for i in range(num_consumers):
        tasks.put(Task(i+num_jobs, i+num_jobs, 'END'))

    print(f'tasks: {tasks.qsize()}')
    # Block until all items in the queue have been gotten and processed.
    tasks.join()

    while num_jobs:
        result = results.get()
        print(f'Result: {result}')
        num_jobs -= 1