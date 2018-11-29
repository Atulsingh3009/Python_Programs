# colon seperated sequence
l = []
for i in range(1,100):
	if i % 7 ==0 and i % 3 != 0:
		l.append(str(i))

print(':'.join(l))	


l = []
for n in range(1,101):
    if n % 7 == 0 and n % 3 != 0:
        l.append(str(n))
print (':'.join(l))