def pal(s):
    s = s.lower()
    if len(s) <= 1:
       return True
    elif s[0] != s[-1]:
       return False
    else:
       return pal(s[1:-1])
myiput=input("enter a string:")
if pal(myiput):
    print(f"{myiput}'is a palindrome.")
else:
    print(f"'{my input}' is not a palindrome.")
