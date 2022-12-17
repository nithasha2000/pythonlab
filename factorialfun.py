def fact(n):
    k=n
    ft=1
    i=1
    while(i<=k):
        ft=ft*i
        i=i+1
    return ft
n=int(input("Enter a number : "))
f=fact(n)
print("Factorial of ",n," is ",f)