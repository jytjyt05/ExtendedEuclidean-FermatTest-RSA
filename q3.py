#yuting ji
import random
import sys
sys.setrecursionlimit(2500)

def Euclid(n1, n2):  
    if n1 == 0: 
        return n2  
    else:
        return Euclid(n2%n1,n1) 

def Extended(n1, n2):  
    if n1 == 0:   
        return 0, 1, n2
    
    x1,y1,gcd = Extended(n2%n1, n1)  
    
    a = y1 - (n2//n1) * x1  
    b = x1  
     
    return a,b,gcd

n=random.randint(1,10**1000)
m=random.randint(1,10**1000)

result_l=list(Extended(n,m))
#print(result_l[0])
print("n is:",n)
print("m is:",m)
print("\ncommon divisor is:",result_l[2])
print("a is:",result_l[0])
print("b is:",result_l[1])
check=n*result_l[0]+m*result_l[1]
if check==result_l[2]:
    print("True")
