# Files reading,writing
''' Using enumerate() function you can iterate 
    through the sequence and retrieve the index position 
    and its corresponding value at the same time. 
    >>> for i,v in enumerate([‘Python’,’Java’,’C++’]):
        print(i,v)
        0 Python
        1 Java
        2 C++  '''

# Here a file is being open read the content and print the  alternate lines of the file  
# fobj = open("file.txt")
# print ("**************Reading the even lines from the text file ********\n")
# for i,v in enumerate(fobj):
	#print(i,v)
	#for printing even line use
	# if i % 2 == 0:
	# 	print(v)
	#for odd lines uncomment the below lines	
	# if i % 2 ==1:
	#     print(i,v)    	

# with open('file.txt') as f:
# 	print ("**************Reading the odd lines from the text file ********\n")
# 	f_c = f.readlines()
# 	li = []
# 	count = 0

    
# for i in f_c:
#     if count % 2 == 1:  #To read even lines just change the value to 1
#     	li.append(i)
#     count += 1
# print(li)
# s = '\n'.join(li)
# print(s)


#a = [1,2,3,4,5,6,7,8,9,10]
b = [2,2,4,5,6,7,8,9,10]
l = []
c = 0

for i in b:
    if c %2 ==1:
        l.append(i)
    c +=1
print(l)        



	

