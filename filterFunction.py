def evenodd(l):
    
        if l%2==0:
            return True
        else:
            return False
l=[0,5,10,15,20,25,30]
print(list(filter(evenodd,l)))
