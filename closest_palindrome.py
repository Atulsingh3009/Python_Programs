# def reverse(num):
#     reverse= 0
#     while num:
#         reverse= reverse*10 + num%10
#         num= num//10
#     return reverse

# num= int(input("Enter any number :- "))
# if num==reverse(num):
#     print ("Already palindrome.")
# else:
#     while True:
#         num+= 1
#         if num==reverse(num):
#             print ("Next palindrome is ", num)
#             break


def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = input('Enter a number: ')
if is_palindrome(n):
   print('Congratulations! {0} is a palindrome.'.format(n))
else:
   n1 = n
   while not is_palindrome(n1):
       n1 = int(n1)+1
   print('Numner entered {0}, but the next palindrome is {1}'.format(n, n1))
