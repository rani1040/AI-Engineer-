import keyword
# special words which cannot be used as variable name
print(keyword.kwlist)

name="riya"
if name=="rani":
    pass # pass means we will write code later


# if you want to print only it 1 , 5
for i in range(0,1000):
    if i==5:
        print(i)
        break

#if you want to skip any value

for i in range(0,10):
    if i==5:
        continue