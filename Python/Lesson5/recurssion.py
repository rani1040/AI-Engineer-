# A recursion has 2 parts:


# Base condition → when to stop
# Recursive call → function calls itself with a smaller problem

# problem statement print 1, 5

def count(num):
    # when to stop-- when it becomes 5
    if num==5: # base condition
        return 
    # calling function
    print(num)
    count(num+1)

# calling function and giving value of num as 5
count(1)