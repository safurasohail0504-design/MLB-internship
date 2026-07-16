num=int(input("Enter num: "))
count=0
while num != 0:
    num=num//10
    count=count+1
print("No of digits:",count)