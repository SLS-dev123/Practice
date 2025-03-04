#a
import random 
i = random.randint(1,90)
j = random.randint(1,90)
list1 = []
list1.append(i)
list1.append(j)
print(list1)
#b
if(i>j):
    print(list1)
else:
    list2 =[]
    i,j = j,i
    list2.append(i)
    list2.append(j)
    print(list2)
#c
list3=[]
for i in range(2,90):
    isprime = 1
    for j in range(2,i):
        if(i%j == 0):
            isprime = 0
            break
    if isprime:
        list3.append(i+2)
print(list3)
#d
list4 = ["","x","x^2","x^3","x^4","x^5"]
for i,j, in enumerate(list4,2):
    print(f"{i}{j}",end =" + ")