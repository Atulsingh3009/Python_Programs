L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

from collections import defaultdict
d = defaultdict(list)
print(d)
for i in L:
	print(i)
	d[len(str(i))].append(i)
print(d)
print ({k:v for k,v in d.items()})	