# #fibonnaci series recursive
# def fib(n):
# 	if n == 0 or n==1:
# 		return n
# 	else:
# 		return fib(n-1) +fib(n-2)

# print(fib(10))


# # fibonnaci series  iterative
# def fib_iter(n):
    
#     # Set starting point
#     a = 0
#     b = 1
    
#     # Follow algorithm
#     for i in range(n):
        
#         a, b = b, a + b
#     return a

# print(fib_iter(10))    	



n = int(input("Enter the no :"))
f = 0
s = 1

for i in range(n):
	#rint(f)
	f, s = s, f + s
	#t = f
	#f = s
	#s = t + s
	print(f)
		