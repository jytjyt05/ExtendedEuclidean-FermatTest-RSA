#yuting ji

resource=('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
def decypher(result,length):
    i=0
    print("Decoded message is:")
    print(result)
    print("Plain text is:")
    while i<length:
        p=str(result)[i:i+2]
        print(resource[int(p)-1])
        i+=2
        
result1=pow(395415567933,14699465729,472221735719)
length1=len(str(result1))
decypher(result1,length1)
##end of first 
##

N=150306660227
e=257

f=2
while N%f!=0:
    f=f+1

p=f
q=N//p
k=(p-1)*(q-1)

def Extended(n1, n2):  
    if n1 == 0:   
        return 0, 1, n2
    
    x1,y1,gcd = Extended(n2%n1, n1)  
    
    a = y1 - (n2//n1) * x1  
    b = x1  
     
    return a,b,gcd

result_list2=Extended(e,k)
d=result_list2[0]+k
print("\nDecrytion exponent is:")
print(d)

result2=pow(58565857117,d,N)
length2=len(str(result2))
decypher(result2,length2)
##end of second
##

def FermatTest(n,trials):
    if trials==0:
        return True
    else:
        if n>3 and pow(random.randint(2,n-2),n-1,n)!=1:
            return False
        else:
            return FermatTest(n,trials-1)

message1=27284682555982882069237
message2=283967477199546905990801
N=124137798108168664109413
e=257

result_list3=Extended(N,message2)
p=result_list3[2]
q=N//p
k=(p-1)*(q-1)
print()
##print(p)
##print(q)
##print(k)
result_list4=Extended(e,k)
d=result_list4[0]

result3=pow(message1,d,N)
length3=len(str(result3))
if length3==10:
    print("Decoded message don't need to add any 0")
else:
    print("Original Decoded message is:")
    print(result3)
    print("In order to translate to plain text, Decoded message needs an additional 0")
    result3="0"+str(result3)
    length3+=1
    
decypher(result3,length3)
##end of 3rd
##
