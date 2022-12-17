n=int(input("Enter a limit : "))
list=[]
sum=0
print("Enter list values : ")
for i in range(0,n):
    e=int(input())
    list.append(e)
    sum=sum+e
print("List : ",list)
print("Sum of list elements are : ",sum)