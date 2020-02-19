import glob

dir_path = input('Input the dir path: ')
head_escape = input('Any head escape characters?: ')
search_pattern = input('Your search pattern in this dir: ')

if dir_path[-1] == '/':
	dir_path = dir_path[:-1]

head_escape_chars = list(head_escape)
search_patterns = []

if len(head_escape_chars) == 0:
	print('Searching without head escaping characters')
	search_patterns = [search_pattern]
else:

	for head_escape_char in head_escape_chars:
		search_patterns += [glob.escape(head_escape_char) + search_pattern]

for pattern in search_patterns:
	pattern = dir_path + '/' + pattern
	print(f'Searching with pattern: {pattern}')
	for name in sorted(glob.glob(pattern)):
		print(name)
	print()
