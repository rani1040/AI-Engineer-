# Rows  →  Outer loop
# Columns → Inner loop
# Printing → What you print inside inner loop

# first pattern star
for row in range(0,5):
    # in 1st row 1  star means 1 colu
    for j in range(0,row):
        print("*", end="")
    # after each row next line
    print()

# pyramid patter
num=6
for row in range(1,num):
    # first row will have spaces and one star
    for space in range(0,num-row):
        print(" ",end="")
    for star in range(0,2*row-1):
        print("*",end="")

    print("")
