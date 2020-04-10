# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-10 16:32:47
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 16:58:06
import signal
import time
import threading

def signal_handler(num, stack):
    print(f"{time.ctime()} Alarm in {threading.currentThread().name}")

signal.signal(signal.SIGALRM, signal_handler)

def use_alarm():
    t_name = threading.currentThread().name
    print(f"{time.ctime()} Setting alarm in {t_name}")
    signal.alarm(1)
    print(f"{time.ctime()} Sleeping in {t_name}")
    time.sleep(3)
    print(f"{time.ctime()} Done with sleep in {t_name}")

alarm_thread = threading.Thread(
    target=use_alarm,
    name='alarm_thread'
    )
alarm_thread.start()
time.sleep(0.1)

print(f"{time.ctime()} Waiting for {alarm_thread.name}")
alarm_thread.join()

print(f"{time.ctime()} Exiting normally")