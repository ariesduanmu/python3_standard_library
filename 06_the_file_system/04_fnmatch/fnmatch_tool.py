import fnmatch
import os

from pprint import pprint

dir_path = input('Input the dir path: ')
search_pattern = input('Your search pattern in this dir: ')
only_filter = input('Only filter the resules?(y/n):')
is_only_filter = only_filter.lower() == 'y'

is_case_sensitive = False
if not is_only_filter:
	case_sensitive = input('Is it case sensitive?(y/n): ')
	is_case_sensitive = case_sensitive.lower() == 'y'

files = sorted(os.listdir(dir_path))

print(f'searching with pattern:{fnmatch.translate(search_pattern)}')

if is_only_filter:
	pprint(fnmatch.filter(files, search_pattern))
else:
	if is_case_sensitive:
		for file in files:
			print(file, fnmatch.fnmatchcase(file, search_pattern))
	else:
		for file in files:
			print(file, fnmatch.fnmatch(file, search_pattern))


