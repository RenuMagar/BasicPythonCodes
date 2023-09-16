def factoroal(num):
    if num==0:
        result=1
    else:
        result=num*factoroal(num-1)
    return result
print("factorial of 4",factoroal(4))
print("factorial of 4",factoroal(5))
