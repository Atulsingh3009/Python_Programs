# Number = 
# Sum = 0
# for i in range(1, Number):
#     if(Number % i == 0):
#         Sum = Sum + i
# if (Sum == Number):
#     print(NUmber)
# else:
#     print(Number)

a = int(input("Number_1 : "))
b =int(input("Number_2 : "))

for n in range(a, b):
    Sum = 0
    for i in range(1, n):
        if(n % i == 0):
            Sum = Sum + i       

    if(Sum == n):
        print(n)    