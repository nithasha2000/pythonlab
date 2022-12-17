n=int(input("Enter a number : "))
a,b=0,1
sum=0
print("Fibonacci series : ")
print(a)
print(b)
for i in range(2,n):
    sum=a+b
    a=b
    b=sum
    print(sum)
    i=i+1
