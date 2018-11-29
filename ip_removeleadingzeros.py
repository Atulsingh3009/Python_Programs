# Remove leading zeros from an IP address

#Method 1  Traversal and Join
def removeZeroes(ip):
 	l = []
 	for i in ip.split('.'):
 		a = str(int(i))
 		#print(a)
 		l.append(a)
 	b = '.'.join(l)
 	print(b)

removeZeroes('10.05.004.34')


# #  Method 2 using List comprehension

# def removeZeros(ip):
# 	new_ip = [str(int(i)) for i in ip.split(".")]  
# 	return new_ip 
     
     
# ip ="100.020.003.400" 
# print(removeZeros(ip))


#  Method 3
'''
import re
def removeZeros(ip):
    new_ip = re.sub(r'\b0+(\d)', r'\1', ip)
    print(new_ip)
    #return new_ip 
     
     
# driver code   
# example1
ip ="100.020.003.400" 
removeZeros(ip)

'''

