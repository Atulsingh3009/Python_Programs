sentence='The Mississippi River'
s =sentence.lower()
count =list(map(s.count,s))
v = []
for i in s:
	v.append(i)
z = list(zip(v,count))
print(z)

print("#####################")

d = dict((c,sentence.count(c)) for c in sentence)
print(d)