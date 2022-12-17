a=input("enter a string")
n=len(a)-1
k=''
while(n>=0):
    k=k+a[n]
    n=n-1
print("reversed string is:",k)