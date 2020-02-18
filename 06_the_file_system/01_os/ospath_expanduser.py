import os.path


'''自动添加用户 '~' 信息
'''
USERS = ['','aries','idk']

for user in USERS:
	lookup = '~' + user
	print("{!r:>15}:{!r}".format(lookup, os.path.expanduser(lookup)))