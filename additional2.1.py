import re
email=input("Enter Email:")
pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
if re.match(pattern,email):
    print("valid Email Address")
else:
    print("invalid Email Address")
