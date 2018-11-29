def hamming(s1,s2): 
    if len(s1) != len(s2): 
        raise ValueError("Not defined - unequal lenght sequences") 
    return sum(c1 != c2 for c1,c2 in zip(s1,s2))

if __name__ == '__main__': 
    print(hamming("karolin", "kathrin")) # 3 
    print(hamming("karolin", "kerstin")) # 3 
    print(hamming("1011101", "1001001")) # 2
    print(hamming("2173896", "2233796")) # 3


s1 = input("Enter the string s1 :")
s2 = input("Enter the string s2 :")

if len(s1) != len(s2):
	print("Strings are of impproper length")
else:
	a = sum(c1 != c2 for c1,c2 in zip(s1,s2))
	print(a)


L1 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
L2 =L1[::1]
print(L2)
