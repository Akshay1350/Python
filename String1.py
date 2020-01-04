s=input("enter some string")
i=0
for x in s:
    print("this character present at +ve index {} and the character at negative index is {}".format(i,i-len(s),x))
    i=i+1
