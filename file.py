from datetime import datetime


with open ('file.txt','r') as f:
	print(f.read())

import os
print(os.path.expanduser('~'))
a = os.getcwd()
print(a)

print(os.path.dirname(a))

cur_dir = os.curdir
print(cur_dir)


a = os.getcwd()
print(a)

b = os.stat('file.txt').st_mtime
print(datetime.fromtimestamp(b))


a = 5
b =10
.__add__(self, b))
print(n)
