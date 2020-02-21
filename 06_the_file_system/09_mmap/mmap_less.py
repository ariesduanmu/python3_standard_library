# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-21 16:16:49
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-21 17:08:33
import mmap
import string
import tempfile
import os
from random import choice

def random_chars():
    choices = list(string.ascii_lowercase)
    return ''.join([choice(choices) for _ in range(200)])

def make_tempfile():
    fd, temp_file_path = tempfile.mkstemp()
    os.close(fd)
    with open(temp_file_path, 'w') as f:
        f.write(random_chars())

    return temp_file_path

def cleanup(filename):
    pathlib.Path(filename).unlink()


step = input('read step: ')
step = int(step)

tempfile = make_tempfile()
with open(tempfile, 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        n = m.read(step)
        print(n)

        while True:
            is_quit = input("Quit?(y/n) ")
            if is_quit.lower() == 'y':
                break
            n = m.read(step)
            print(n)
            
            if not n:
                print(f"Finish")
                break

cleanup(tempfile)
