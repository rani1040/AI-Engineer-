import random
moves = ["rock","paper","scissor"]
computer = random.choice(moves)
print("choose from this moves:",moves)
user = input("enter your move: ").lower()
if user=="rock":
    if computer=="scissor":
        print("computer wins")
    elif computer=="paper":
        print("you win")
    else:
        print("draw")
elif user=="paper":
    if computer=="scissor":
        print("you wins")
    elif computer=="rock":
        print("computer win")
    else:
        print("draw")
elif user=="scissor":
    if computer=="rock":
        print("computer wins")
    elif computer=="paper":
        print("you win")
    else:
        print("draw")