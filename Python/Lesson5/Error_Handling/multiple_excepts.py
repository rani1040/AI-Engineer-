
try:
    n1= int(input("enter number 1 :"))
    n2 = int(input("enter number 2 :"))
    ans = n1/n2
except ZeroDivisionError:
    print("Division by zero is error !!")
except ValueError:
    print("Please enter valid whole numbers")
except:
    print("Wrong input")