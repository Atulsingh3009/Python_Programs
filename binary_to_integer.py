# # Converting binary to integer
# s1 "0100,0011,1010,1001"
# s2 = s1.split(',')
# num = []
# for s in s2:
# 	n = 0
# 	for i,v in enumerate(s[::-1]):
# 		n + = (2** int(i)) * int(v)
# 	num.append(n)
# print(num)



s1 = "0100,0011,1010,1001"
s2 = s1.split(',')
print(s2)

a1 = "0100,0011,1010,1001"
a2 = a1.split(',')
print(a2)
num = []
for s in a2:
	n = 0
	#print(s)

	
	for i,v in enumerate(s[::-1]):
		#print(int(v))
		#print(int(i))

		n += (2**int(i))* int(v)
	num.append(n)
print(n)		
