# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-03-12 09:45:03
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-03-12 09:46:25
import subprocess

proc = subprocess.Popen(
    ['python', '-m', 'dis', 'dis_sample.py'],
    stdout=subprocess.PIPE,
    )
stdout_value = proc.communicate()[0].decode('utf-8')
print(stdout_value)