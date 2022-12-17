a=int(input("enter a number"))
n=a
r=0
while(n>0):
    s=n%10
    r=r*10+s
    n=n//10
if(r==a):
        print(a,"is palindrome")
else:
        print(a,"is not palindrome")