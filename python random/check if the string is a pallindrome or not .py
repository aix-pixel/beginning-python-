str = input("enter the string ")
if str==str[::-1]:
    print("string is in pallindrome")
else:
    print("not in pallindrome")    


def pallindrome(s):
    return s==s[::-1]

print(pallindrome("madam"))    