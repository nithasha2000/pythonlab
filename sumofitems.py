a=int(input("Enter the limit : "))
l=[]
sum=0
print("Enter the elements in the list : ")
for i in range(a):
    a=int(input())
    l.append(a)
    sum=sum+l[i]
print(l)
print("Sum of elements in the list =",sum)
