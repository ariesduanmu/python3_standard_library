# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-10 16:32:33
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 17:11:29
import signal
import threading
import os
import time

print('My PID is:', os.getpid())

def signal_handler(num, stack):
    print(f'{time.ctime()} Received signal {num} in {threading.currentThread().name}')

def alarm_handler(num, stack):
    print(f"{time.ctime()} ALARM in {threading.currentThread().name}")
    raise SystemExit('Exiting')

signal.signal(signal.SIGUSR1, signal_handler)
signal.signal(signal.SIGALRM, alarm_handler)

def wait_for_signal():
    print(f'{time.ctime()} Waiting for signal in {threading.currentThread().name}')
    signal.pause()
    print('{time.ctime()} Done waiting')

receiver = threading.Thread(
    target=wait_for_signal,
    name='receiver'
    )

receiver.start()
time.sleep(0.1)

def send_signal():
    print(f'{time.ctime()} Sending signal in {threading.currentThread().name}')
    os.kill(os.getpid(), signal.SIGUSR1)


sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()


print(f'{time.ctime()} Waiting for {receiver.name}')
signal.alarm(2)
receiver.join()