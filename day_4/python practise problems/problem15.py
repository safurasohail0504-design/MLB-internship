for n in range(1,101): 
    is_prime=True
    if n<=1:
        is_prime=False
    else:
        for i in range(2,n):       
            if n % i == 0:           
                is_prime=False
                break                
    if is_prime:
        print(n)
