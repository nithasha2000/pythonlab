list=[]
n=int(input("Enter the limit : "))
print("Enter the list of integers :")
for i in range(0,n):
    val=int(input())
    if(val>100):
        list.append("over")
    else:
        list.append(val)

print("New List :",list)