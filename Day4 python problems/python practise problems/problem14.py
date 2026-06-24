n=int(input("enter num:"))
is_prime=True
for i in range(2, n):       
    if n % i == 0:           
        is_prime=False
        break                
if is_prime:
    print("Prime")
else:
    print("Not Prime")