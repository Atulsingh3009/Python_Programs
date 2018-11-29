# Merge two sorted list 
#Solution -1
a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
c = []

while a and b:
	if a[0] < b[0]:
		c.append(a.pop(0))
	else:
		c.append(b.pop(0))

print(c+a+b)		


# solution-2

a.extend(b)
print(sorted(a))

# merge sorted list with unique elements
first_list = [3, 4, 6, 10, 11, 18]
second_list = [1, 5, 7, 11, 13, 19, 21]
newList = []
for i in first_list:
	newList.append(i)
for z in second_list:
	if z not in newList:
		newList.append(z)
newList.sort()
print (newList)



#find common elements from two list
def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

list1 = [1,2,3,4]
list2 = [2,3,4,5,6]
print(common_elements(list1,list2))


def common_elements(list1, list2):
    return [element for element in list1 if element in list2]