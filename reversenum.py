n=int(input("Enter the number : "))
r=0
t=n
while n!=0:
    d=n%10
    r=r*10+d
    n=n//10
print("Reverse of ",t," is ",r)