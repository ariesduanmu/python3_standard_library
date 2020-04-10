# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-10 16:10:06
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-10 16:34:02
import signal

def alarm_received(n, stack):
    print("Received: ", n)
    return

signal.signal(signal.SIGALRM, alarm_received)

signal_to_names = {
    getattr(signal, n): n
    for n in dir(signal)
    if n.startswith('SIG') and '_' not in n
}

# show all signal handlers
for s, name in sorted(signal_to_names.items()):
    handler = signal.getsignal(s)
    if handler is signal.SIG_DFL:
        handler = 'SIG_DFL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN'

    print(f'{name:<10} ({s:2d})', handler)