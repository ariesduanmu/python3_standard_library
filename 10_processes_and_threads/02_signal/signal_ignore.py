# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-10 16:25:09
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 16:34:55
import signal
import os
import time

def do_exit(sig, stack):
    raise SystemExit('Exiting')


# ctrl+c not working for exit anymore
signal.signal(signal.SIGINT, signal.SIG_IGN)

# use another terminal type kill -USR1 $pid to exit
signal.signal(signal.SIGUSR1, do_exit)

print(f'My PID: {os.getpid()}')

signal.pause()