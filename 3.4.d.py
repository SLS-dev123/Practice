num = eval(input("enter a number: "))
k = 1
l=2
count = 0
while(num != count):
    for i in range(l,(k+1)):
        isprime = True
        for j in range(2,(i//2)+1):
            if i%j == 0:
                isprime = False
                break
        if isprime :
            print(i)
            count +=1
    l=k+1
    k +=1 