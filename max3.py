# Highest possible product
#Find the highest possible product that we can get by multiplying any 3 numbers from an input array:


def mx3(a):
	b = sorted(a)

	mo = b[0]
	m1 = b[1]
	x1 = b[-1]
	x2 = b[-2]
	x3 = b[-3]

	if mo< 0 and m1 < 0:
		return max(mo*m1*x1*x2*x3)
	else:
		return x1*x2*x3

l1 = [10,20,5,2,7,9,3,4] 
print(mx3(l1))
