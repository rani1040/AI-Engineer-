import random
computer = random.randint(1,10)
while True:
    user = int(input("enter number between 1,10: "))
    if user==computer:
        print("correct guess")
        break
    elif user>computer:
        print("enter lower number")
    else:
        print("enter higher number")
    
