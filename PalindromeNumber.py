num=int(input("enter a number"))
temp=num
reverse=0
while temp>0:
    reminder=temp%10
    reverse=(reverse*10)+reminder
    temp=temp//10
    
if num==reverse:
    print("palindrome")
else:
    print("not palindrome")
