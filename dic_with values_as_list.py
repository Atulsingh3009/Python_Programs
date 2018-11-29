cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

d2 = {}
for k,v in cities.items():
	#print(k)
	#print(v)
	d2.setdefault(v,[]).append(k)
print(d2)	

numbers = [1,256,64,65536,186000,1024,8,16,1905]
d = {}

for n in numbers:
	d.setdefault(len(str(n)),[]).append(n)
print(d)	



