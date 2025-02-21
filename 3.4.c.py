num = eval(input("enter a number: "))
for i in range(2,(num+1)):
    isprime = True
    for j in range(2,(i//2)+1):
        if i%j == 0:
            isprime = False
            break
    if isprime :
        print(i)