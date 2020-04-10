# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-10 16:20:29
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 16:33:49
import signal
import time

# signal will interupt the sleep
def receive_alarm(signum, stack):
    print(f"Alarm: {time.ctime()}")

signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)

print(f"Before: {time.ctime()}")
time.sleep(4)
print(f"After: {time.ctime()}")