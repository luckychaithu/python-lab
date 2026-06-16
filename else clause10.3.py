try:
    num=int(input("enter a number:"))
    result=10/num
except valueError:
        print("Error:invalid input!please enter a valid number.")
except zeroDivisionError:
        print("Error:Division by zero!")
else:
        print("result:",result)
                
