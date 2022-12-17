n=int(input("Enter the limit : "))
sum_o=sum_e=0
i=1
while i<=n:
    if i%2==0:
        sum_e=sum_e+i
    else:
        sum_o=sum_o+i
    i=i+1
print("sum of even numbers:",sum_e)
print("sum of odd numbers:",sum_o)