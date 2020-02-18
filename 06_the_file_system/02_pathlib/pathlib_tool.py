import pathlib
import os
import sys
import shutil
import time

FIRST_DIR = 'first'
SECOND_DIR = 'second'
NEW_FILE = 'pathlib_test'
CHANGE_FILE = 'test'

def sys_type():
	if os.sep == '/':
		return 0
	else:
		return 1

dir_path = input('Input the dir path: ')

# resolve
dir_path = pathlib.Path(dir_path).resolve()

sys_t = sys_type()

# operator
if sys_t == 0:
	user_dir_path = pathlib.PurePosixPath(dir_path)
else:
	user_dir_path = pathlib.PureWindowsPath(dir_path)

# join path
subdirs = [FIRST_DIR, SECOND_DIR]
new_user_dir_path =  user_dir_path.joinpath(*subdirs)

new_file_path_1 = user_dir_path / NEW_FILE
new_file_path_2 = new_user_dir_path / NEW_FILE

# sorry I change my mind
change_file_path_2 = new_file_path_2.with_name(CHANGE_FILE)

# sorry I change my mind again
change_file_path_1 = new_file_path_1.with_suffix('.py')
change_file_path_2 = change_file_path_2.with_suffix('.txt')

print(f'New File Path 1: ')
print(f'path   : {change_file_path_1}')
print(f'name   : {change_file_path_1.name}')
print(f'suffix : {change_file_path_1.suffix}')
print(f'stem   : {change_file_path_1.stem}')
print()
print(f'New File Path 2: ')
print(f'path   : {change_file_path_2}')
print(f'name   : {change_file_path_2.name}')
print(f'suffix : {change_file_path_2.suffix}')
print(f'stem   : {change_file_path_2.stem}')
print()

root_path = pathlib.Path(f'{user_dir_path}')

# I wanna delete all file/dir having the same name

duplicated_change_file_1 = root_path.rglob(f'{NEW_FILE}.py')
duplicated_change_file_2 = root_path.rglob(FIRST_DIR)


for f in duplicated_change_file_1:
	override = input(f"{f} existing, do you want override it?(y/n): ")
	if override.lower() == 'y':
		# just delete it
		print(f'Removing {f}')
		f.unlink()
	else:
		sys.exit(0)

for f in duplicated_change_file_2:
	override = input(f"{f} existing, do you want override it?(y/n): ")
	if override.lower() == 'y':
		# just delete it
		print(f'Removing {f}')
		try:
			f.rmdir()
		except:
			# use shutil
			shutil.rmtree(str(f))
	else:
		sys.exit(0)

change_file_path_1 = pathlib.Path(str(change_file_path_1))
change_file_path_1.write_bytes(b'#!/usr/bin/env python3\nprint("Well Done")')

change_file_path_2 = pathlib.Path(str(change_file_path_2))
# create dirs
(root_path / FIRST_DIR).mkdir()
(root_path / FIRST_DIR / SECOND_DIR).mkdir()

change_file_path_2.write_bytes(b'insert')

# properties

stat_info_1 = change_file_path_1.stat()

print(change_file_path_1)
print(f'Size : {stat_info_1.st_size}')
print(f'Permissions : {stat_info_1.st_mode}')
print(f'Owner : {stat_info_1.st_uid}')
print(f'Device : {stat_info_1.st_dev}')
print(f'Created : {time.ctime(stat_info_1.st_ctime)}')
print(f'Last modified : {time.ctime(stat_info_1.st_mtime)}')
print(f'Last accessed : {time.ctime(stat_info_1.st_atime)}')
print()

stat_info_2 = change_file_path_2.stat()
print(change_file_path_2)
print(f'Size : {stat_info_2.st_size}')
print(f'Permissions : {stat_info_2.st_mode}')
print(f'Owner : {stat_info_2.st_uid}')
print(f'Device : {stat_info_2.st_dev}')
print(f'Created : {time.ctime(stat_info_2.st_ctime)}')
print(f'Last modified : {time.ctime(stat_info_2.st_mtime)}')
print(f'Last accessed : {time.ctime(stat_info_2.st_atime)}')
print()