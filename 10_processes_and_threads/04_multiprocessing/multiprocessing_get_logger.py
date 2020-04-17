# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-04-17 09:11:53
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-04-17 09:17:04
# 10.4.8 Logging

import multiprocessing
import logging
import sys

def worker():
    print('Doing some work')
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    p = multiprocessing.Process(name='log test', target=worker)
    p.start()
    p.join()