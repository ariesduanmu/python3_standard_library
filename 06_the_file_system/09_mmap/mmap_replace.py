# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-21 16:17:20
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-21 17:20:42
import mmap
import shutil
import tempfile
import os
import pathlib


def make_tempfile():
    text = "Hello World"
    fd, temp_file_path = tempfile.mkstemp()
    os.close(fd)
    with open(temp_file_path, 'w') as f:
        f.write(text)

    return temp_file_path


def cleanup(filename):
    pathlib.Path(filename).unlink()

name = input("What's your name?")
temp_file_path = make_tempfile()

with open(temp_file_path, 'r+') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY) as m:
        print(f'Before:\n{m.readline().rstrip()}')
        m.seek(0)

        loc = m.find(b'World')
        m[loc:loc+len('World')] = name.encode()
        m.flush()
        print(f'After:\n{m.readline().rstrip()}')

cleanup(temp_file_path)