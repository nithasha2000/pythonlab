n=int(input("Enter a number to which square should be calculated :"))
list=[]
for i in range(1,n+1):
    list.append(i)
print("The list of numbers are : ")
print(list)
print("The square of numbers in the above list are :")
newlist=[i**2 for i in list if i<n+1]
print(newlist)
