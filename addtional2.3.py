import re
text="devops123"
if re.match(r'^[A-Za-z0-9]+$',text):
    print("alphanumeric string")
else:
        print("not alphanumeric")
