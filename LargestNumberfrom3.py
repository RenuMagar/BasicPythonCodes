#read three numbers from three keyboard and print largest value
a=int(input("enter a number"))
b=int(input("enter a 2nd number"))
c=int(input("enter a 3rdnumber"))
if a>b and a>c:
    print(" a is max",a)
elif b>c:
    print("b is max",b)
else:
    print("c is max",c)
