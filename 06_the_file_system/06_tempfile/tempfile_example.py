# -*- coding: utf-8 -*-
# @Author: Li Qin
# @Date:   2020-02-21 09:38:43
# @Last Modified by:   Li Qin
# @Last Modified time: 2020-02-21 10:01:30
import tempfile
import pathlib

print(f"Default directory that hold the temporary files: {tempfile.gettempdir()}")
print(f"String prefix for new file and dir: {tempfile.gettempprefix()}")

# custom temp file
with tempfile.TemporaryDirectory() as directory_name:
    the_dir = pathlib.Path(directory_name)
    print(f"Temp dir: {directory_name}")
    with tempfile.NamedTemporaryFile(suffix='_suffix',
                                     prefix='prefix_',
                                     dir=directory_name) as temp:
        print(f"Custom tempfile: {temp.name}")
        the_file = pathlib.Path(temp.name)

print(f"Temp Dir exists after? {the_dir.exists()}")
print(f"Custom tempfile exists after? {the_file.exists()}")

# For temporary files containing relatively small amounts of data, it is likely to be more
# efficient to use a SpooledTemporaryFile because it holds the file contents in memory using
# an io.BytesIO or io.StringIO buffer until the data reaches a threshold size. When the
# amount of data passes the threshold, it is “rolled over” and written to disk, and then the
# buffer is replaced with a normal TemporaryFile().

with tempfile.SpooledTemporaryFile(max_size=200, mode='w+t', encoding='utf-8') as temp:
    print(f'Temp name: {temp.name}')
    for i in range(10):
        # pass the threshold in the middle, the rest will be omit
        temp.write('testing abcdefghijklmnopqrstuvwxyz\n')
        print(temp._rolled, temp._file)
    temp.seek(0)
    print(temp.read())
