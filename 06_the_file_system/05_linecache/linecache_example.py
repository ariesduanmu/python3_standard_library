import os
import pathlib
import tempfile
import linecache
import string 
from random import choice

def random_chars():
	choices = list(string.ascii_lowercase)+[' ','\n']
	return ''.join([choice(choices) for _ in range(2000)])

def make_tempfile():
	fd, temp_file_path = tempfile.mkstemp()
	os.close(fd)
	with open(temp_file_path, 'w') as f:
		f.write(random_chars())

	return temp_file_path

def cleanup(filename):
	pathlib.Path(filename).unlink()

tmp_file = make_tempfile()

print(tmp_file)
lines = [1,3,10,100,1000]
for l in lines:
	print(f"line: {l}")
	print(linecache.getline(tmp_file, l))
	print()
cleanup(tmp_file)

