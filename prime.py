a=int(input("enter a number"))
i=2
f=0
while(i>a):
    if(a%i==0):
        f=1
        i=i+1
if(f==0):
    print(a,"is prime")
else:
    print(a,"is not prime")






