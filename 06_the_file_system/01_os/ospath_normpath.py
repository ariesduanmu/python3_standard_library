import os.path

'''规整路径
'''
SEP = os.sep

PATHS = [
SEP.join(['one','two','three']),
SEP.join(['one','.','two','.','three']),
SEP.join(['one','..','alt','two','three']),
]

for path in PATHS:
	print('{!r:>26} : {!r}'.format(path, os.path.normpath(path)))