#yuting ji
import random

def FermatTest(n,trials):
    if trials==0:
        return True
    else:
        if n>3 and pow(random.randint(2,n-2),n-1,n)!=1:
            return False
        else:
            return FermatTest(n,trials-1)

def FermatPrime(max,trials):
    n=random.randint(4,max)
    while not FermatTest(n,trials):
        n=random.randint(2,max)
    return n

f=FermatPrime(10**1000,10)
print(f)


