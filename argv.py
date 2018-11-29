from sys import argv

arr = argv
print(arr)
arr.pop(0)
print(arr)
n = len(arr)


def rearrange(arr, n):
 
    for i in range(n - 1):
        if (i % 2 == 0 and arr[i] > arr[i + 1]):
         
            temp = arr[i]
            arr[i]= arr[i + 1]
            arr[i + 1]= temp
         
        if (i % 2 != 0 and arr[i] < arr[i + 1]):
          
            temp = arr[i]
            arr[i]= arr[i + 1]
            arr[i + 1]= temp
            
  
# Utility that prints out an array in
# a line 
def printArray(arr, size):
 
    for i in range(size):
        print(arr[i], " ", end ="")
  
    print()
 
# Driver code
 
  
print("Before rearranging: ")
printArray(arr, n)
  
rearrange(arr, n)
  
print("After rearranging:")
printArray(arr, n)

