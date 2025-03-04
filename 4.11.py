def arrange(x,ys):
    newlist = []
    j=0
    notfound=1
    for i in ys:
        if x > i:
            newlist.append(i)
            notfound = 0
        elif(ys[j-1]<x and i>x):
            newlist.append(x)
        elif(i>x):
            newlist.append(i)
        j +=1
    if(notfound == 1):
        y= ys+[x]
        print(y)
    else:
        print(newlist)
x = int(input("enter a the value of x: "))
ys1 = eval(input("enter as list of numbers: ")).split(" ")
ys2 = list(map(int,ys1))
ys = sorted(ys2)
arrange(x,ys)