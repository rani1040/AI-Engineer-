num = 4
is_prime=True

for i in range(2,num):
    if num%i==0:
        is_prime=False
        break

if is_prime:
    print("it is prime number")
else:
    print("not prime")