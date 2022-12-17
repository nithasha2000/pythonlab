n=int(input("Enter a number : "))
a,b=0,1
sum=0
print("Fibonacci series : ")
print(a)
print(b)
sum=a+b
for i in range(sum,n-1):
    print(sum)
    a=b
    b=sum
    sum=a+b


