# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 10:36:04
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 10:37:31
i = 1
j = 0
k = 3

try:
    result = k * (i / j) + (i / k)
except:
    import sys
    import dis
    exc_type, exc_value, exc_tb = sys.exc_info()
    dis.distb(exc_tb)