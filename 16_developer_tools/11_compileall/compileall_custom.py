# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-24 09:06:23
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-24 10:14:19
import compileall
import glob
import re
import timeit


def show(title):
    print(title)
    for filename in glob.glob('example/**', recursive=True):
        print(f'  {filename}')
    print()

def compile_():
    show('BEFORE')

    compileall.compile_dir(
        'example',
        maxlevels=0)

    compileall.compile_file('example/subfolder2/c.py')
    show('AFTER')

compile_()