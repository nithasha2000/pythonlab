list1=[]
list2=[]
sum1=0
sum2=0
n1=int(input("Enter the limit of 1st string : "))
print("Enter the values of 1st string : ")
for i in range(0,n1):
    val1=int(input())
    list1.append(val1)
    sum1=sum1+list1[i]
n2=int(input("Enter the limit of 2nd list : "))
print("Enter the values of 2nd string : ")
for i in range(0,n2):
    val2=int(input())
    list2.append(val2)
    sum2=sum2+list2[i]
print("List1 :",list1)
print("List2 :",list2)
if(n1==n2):
    print("List1 and List2 are of same length")
else:
    print("list1 and List2 are not same length")
if(sum1==sum2):
    print("List1 and List2 sums up to same value")
    print("Sum of both lists : ",sum1)
else:
    print("list1 and List2 doesn't sum up to same value")
    print("Sum of 1st List:",sum1)
    print("Sum of 2nd List:",sum2)
check=set(list1) and set(list2)
if check:
    print("Common elements found")
else:
    print("No common elements found")




