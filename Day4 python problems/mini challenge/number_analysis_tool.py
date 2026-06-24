num=int(input("Enter a number: "))
if num%2==0:
    even_odd ="Even"
else:
    even_odd ="Odd"
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
temp1=num   
digit_count=0
while temp1!=0:
    temp1=temp1//10
    digit_count=digit_count + 1
temp2=num
reverse_num=0
while temp2!=0:
    digit=temp2%10
    reverse_num=reverse_num*10+digit
    temp2=temp2//10
if reverse_num==num:
    palindrome="Yes"
else:
    palindrome="No"
print("Number:", num)
print("Even or Odd:", even_odd)
if is_prime:
    print("Prime")
else:
    print("not Prime")
print("Digit Count:", digit_count)
print("Reversed:", reverse_num)
print("Palindrome:", palindrome)