x0 = int(input("enter a x0: "))
xi=103
while xi != 1:
    if(x0%2 == 0):
        xi = x0/2
        print(xi,end =" ")
    else:
        print(x0)
        xi = 3*x0 + 1
        print(xi,end=" ")
    x0 =xi