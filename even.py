n=int(input("Enter the limit : "))
list=[]
print("Enter the values : ")
for i in range(0,n):
    val=int(input())
    if val % 2 != 0:
        list.append(val)
print(" New List : ",list)

