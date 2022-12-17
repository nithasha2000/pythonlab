while True:
    print("select any one of the following operations")
    print("1.add numbers")
    print("2.subtract numbers")
    print("3.divide numbers")
    print("4.multiply numbers")
    print("press 0 to exit")
    choice =int(input("enter an option"))
    if choice == 0:
        break
    if choice == 1:
        a = int(input("enter a number"))
        b = int(input("enter another number"))
        print("sum of ", a, " ", b, " is ", (a + b))
    elif choice == 2:
        a = int(input("enter a number"))
        b = int(input("enter another number"))
        print("difference of ", a, " ", b, " is ", (a - b))
    elif choice == 3:
        a = int(input("enter a number"))
        b = int(input("enter another number"))
        print("quotient of ", a, " ", b, " is ", (a / b))
    elif choice == 4:
        a = int(input("enter a number"))
        b = int(input("enter another number"))
        print("product of ", a, " ", b, " is ", (a * b))
    else:
        print("invalid choice")


