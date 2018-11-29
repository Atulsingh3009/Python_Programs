a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])


############################
'''
a =[1,2,3,7,9,23]
o=[]
e=[]
for i in a:
	if i%2 == 0:
		e.append(i)
	else:
	    o.append(i)	

print(e)
print(o)
'''
##############################
'''
#Python Program to Merge Two Lists and Sort it
a = [1,2,3]
b = [6,2,1]
#a.extend(b)
c=a+b
print(c)
c.sort()
print(c)
'''
############################
'''
#Python Program to Sort the List According to the Second Element in Sublist

a=[['A',34],['B',21],['C',26]]
#print(len(a))
for i in range(0,len(a)):
    #print(i)
    for j in range(0,len(a)-i-1):
        #print(j)
        #print(a[j][1])

        #print(a[j+1][1])
        #print(a[j])
        print(a[j+1])
        #if(a[j][1]>a[j+1][1]):
            #temp=a[j]
            #a[j]=a[j+1]
            #a[j+1]=temp
 
#print(a)
'''
###########################################
'''
a = ['abcewqfeewqfeqfeeqfqfqfq','atul','efheoifhewofhe','fewoifewoifhgwoieghgoihgghw']
a.sort(key=len)
print(a)

'''

##########################################
'''
#join a list
a = ['A','T','U','L']
b=''.join(a)
print(b)
'''
########################################
#program to find subdtring inside a string
'''
string=input("Enter string:")
sub_str=input("Enter word:")
print(string.find(sub_str))
if(string.find(sub_str)== -1):
      print("Substring not found in string!")
else:
      print("Substring in string!")

'''      
###########################################
'''

a =[]
string = input("Enter the string :")
word = input("Ente the word to find : ")
count = 0
a=string.split(" ")
print(a)

c = a.count(word)
print(c)
'''
'''
for i in range(0,len(a)):
	if(word==a[i]):
            count=count+1
print("Count of the word is:")
print(count)
'''

###########################################
''' The program takes a string and forms a new string made of the first 2 characters and last 2 characters from a given string.'''
'''
a =[]
string = input("Enter the string :")
a = len(string)
c = string[0:2]+string[a-2:a]
print(c)
#a=string.split(" ")
#print(a)

#c = a.count(word)
#print(c)

'''
###############################################
'''
string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)
'''
################################################
# seq = ('name', 'age', 'sex')

# dict = dict.fromkeys(seq)
# print ("New Dictionary : %s" %  str(dict))

# dict = dict.fromkeys(seq,(10,2,3))
# print ("New Dictionary : %s" %  str(dict))

################################################3

