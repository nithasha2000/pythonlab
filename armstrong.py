a=int(input("enter a number"))
n=a
r=0
while(n>0):
    s=n%10
    r=r+(s*s*s)
    n=n//10
if(r==a):
        print(a,"is armstrong")
else:
        print(a,"is not armstrong")