n1=int(input("enter the range1: "))
n2=int(input("enter the range2:"))
for num in range(n1,n2+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>=0:
        digit=temp%10
        sum=(sum+digit)**order
        temp=temp//10
    if num == sum:
        print(num)