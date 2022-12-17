cyear=int(input("Enter the current year : "))
fyear=int(input("Enter a future year to calculate leap year : "))
print("Leap years between ",cyear," and ",fyear," are :")
for i in range(cyear,fyear):
    if(i%400==0) or (i%4==0 and i%100!=0):
        print(i)


