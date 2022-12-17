n=int(input("Enter the no:of strings : "))
l=[]
c=0
print("Enter the strings : ")
for i in range(n):
    n=str(input())
    l.append(n)
print(l)
for i in l:
    for j in i:
        if j=='a':
            c=c+1
print("Number of a's in strings : ",c)