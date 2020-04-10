# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-10 15:12:07
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 16:05:53
import signal
import os
import time

def receive_signal(signum, stack):
    print("Received: ", signum)

# only work in *nix
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

print('My PID is:', os.getpid())
while True:
    print("Waiting...")
    time.sleep(3)

# open another terminal
# kill -USR1 $pid
# kill -USR2 $pid
# kill -INT $pid