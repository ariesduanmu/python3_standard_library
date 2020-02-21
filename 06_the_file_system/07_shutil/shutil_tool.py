# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-21 10:43:18
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-21 15:46:10

import shutil
import os
import tempfile
import glob
import pathlib
from time import sleep

gib = 2 ** 30


search_dir_path = input('Input the search dir path: ')
target_dir_path = input('Input the target dir path: ')

target_total_b, target_used_b, target_free_b = shutil.disk_usage(target_dir_path)

print('Target dir path:')
print(f'Total: {target_total_b / gib :6.2f} GiB')
print(f'Used: {target_used_b / gib :6.2f} GiB')
print(f'Free: {target_free_b / gib :6.2f} GiB')

print()

# create tmp dir

tmp_dir = tempfile.gettempdir()
with tempfile.TemporaryDirectory() as directory_path:

    # find file
    pattern = input('Input the search pattern: ')

    # copy file to new dir
    print(search_dir_path + os.sep + pattern)
    for path in glob.glob(search_dir_path + os.sep + pattern):
        print(f"coping {path}")
        shutil.copy2(path, directory_path)

    # archive
    print(directory_path)
    tmp_dir_name = os.path.basename(directory_path)
    os.chdir(tmp_dir)
    shutil.make_archive(
        'example', 'zip',
        root_dir='.',
        base_dir=tmp_dir_name
        )


# unpack in other place
zip_path = os.path.join(tmp_dir, 'example.zip')
shutil.unpack_archive(
    zip_path,
    extract_dir=target_dir_path
    )

# remove zip package
pathlib.Path(zip_path).unlink()

target_unpack_path = os.path.join(target_dir_path, tmp_dir_name)
remove_dir = input(f'Remove {target_unpack_path} now?(y/n) ')
if remove_dir.lower() == 'y':
    # remove old dir
    shutil.rmtree(target_unpack_path)