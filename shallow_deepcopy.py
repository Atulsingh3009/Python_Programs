l = [1,2,3,4,5,6,7,8,9]
newl = l
copiedl = l[:]
newl.append(10)
print(l,id(l))
print(newl,id(newl))
print(copiedl,id(copiedl))

colours1 = ["red", "blue"]
colours2 = colours1
colours2[1] = "green"
print(colours1)
print(colours2)


#copy with slice operator
list1 = ['a','b','c','d']
list2 = list1[:]
list2[1] = 'x'
print(list2)
print(list1)



print("#####################")
l1 = ['a','b',['ab','ba']]
l2 = l1[:]
l2[0] = 'c'
print(l1)
print(l2)


l2[2][1] = 'd'
print(l1)
print(l2)

