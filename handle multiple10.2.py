try:
    num=int(input("enter a number:"))
    result=10/num
    print("result:",result)
except valueError:
        print("error:invalid input!please enter a valid number.")
except zeroDivisionError:
        print("error:Division by zero!")
            
