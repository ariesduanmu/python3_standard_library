# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-13 10:55:27
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-13 10:56:22
import threading

lock = threading.RLock()
print(f'First try: {lock.acquire()}')
print(f'First try: {lock.acquire(0)}')