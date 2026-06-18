mylist=input("enter a list of numbre separated by space:")
mylist=list(map(int,mylist.split()))
sum=0
for num in mylist:
    sum+=num
    print("the sum of the numbers is:",sum)
