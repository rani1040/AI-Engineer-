# age = int(input("Enter your age: "))
# if you enter string you will get error : ValueError: invalid literal for int() with base 10: 'f'

try:
    age = int(input("Enter your age: "))

except:
    print("enter valid  number")

try:
    grade = int(input("enter your grade: "))
except ValueError as e:
    print(e)

