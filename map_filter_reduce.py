l = [x for x in range(10) if x%2 == 0]
print(l)

items = [1, 2, 3, 4, 5]
def sqr(x):
	return x**2

print(list(map(sqr,items)))
print(list(map(lambda x: x**2,items)))


def square(x):
        return (x**2)
def cube(x):
        return (x**3)

funcs = [square, cube]
for r in range(5):
    value =list( map(lambda x: x(r), funcs))
    print (value)


from operator import add
x = [1,2,3]
y = [4,5,6]

z =tuple(map(add,x,y))
print(z)

from itertools import zip_longest
g = list(zip_longest(x,y))
print(g)


a = [1,1,2,3,4,5,6,6,6,3,8,8,7]
b= []
for i in a:
	if a not in b:
		b.append(i)
print(b)		