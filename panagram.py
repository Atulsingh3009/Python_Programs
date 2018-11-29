def checkPangram(s):
    List = []
    # create list of 26 charecters and set false each entry
    for i in range(26):
        List.append(False)


    for c in s.lower(): 
        if not c == " ":
            # make the corresponding entry True
            List[ord(c) -ord('a')]=True

    for ch in List:
        if ch == False:
            return False
    return True



s = "The quick brown fox jumps over the lazy dog"
print(checkPangram(s))            




