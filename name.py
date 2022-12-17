list=[]
count=0
n=int(input("Enter the limit : "))
print("Enter the list of names :")
for i in range(0,n):
    name=input()
    list.append(name)
    for i in list:
        name.split(",")
        if(name[i]=='a'):
            count=count+1
            print("No:of occurences of a in",name,"is",count)
print("New List :",list)
