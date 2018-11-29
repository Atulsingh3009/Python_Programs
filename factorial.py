#factorial

num = int(input("Enter the number :"))
factorial = 1
for i in range(1,num+1):
	factorial = factorial *i
	print(factorial)  # n =5  -> 1,2,6,24,120	

print(factorial) # n=5 -> 120


# Using recursion 

def fact(n):
	if n == 0:
		return 1
	return n*fact(n-1)

n = int(input("Enter the number  : "))	
print(fact(n))


		
