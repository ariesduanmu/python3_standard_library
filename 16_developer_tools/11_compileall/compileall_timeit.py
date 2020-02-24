# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-24 10:13:42
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-24 10:14:52
import timeit

t = timeit.Timer("compile_()", "from compileall_custom import compile_")
print(t.timeit(number=10))