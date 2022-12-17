a=int(input("Enter a number : "))
n=a
r=0
for i in range(n,0,-1):
    s=n%10
    r=r+(s*s*s)
    n=n//10
if(r==a):
        print(a,"is armstrong")
else:
        print(a,"is not armstrong")