#inputing student details
name=input("enter student name")
sub1=int(input("enter mark of subject 1(out of 100)"))
sub2=int(input("enter mark of subject 2(out of 100)"))
sub3=int(input("enter mark of subject 3(out of 100)"))
sub4=int(input("enter mark of subject 4(out of 100)"))
sub5=int(input("enter mark of subject 5(out of 100)"))
total=sub1+sub2+sub3+sub4+sub5 #calculating total marks of student
percent=(total/500)*100
print("name:",name)
print("total marks: ",total," percentage scored : ",percent)


