original=int(input("enter a num:"))
temp=original
reverse=0
while temp!=0:
    digit=temp%10
    reverse=reverse*10+digit
    temp=temp//10
if(reverse==original):
    print("palindrome")
else:
    print("not a palindrome")