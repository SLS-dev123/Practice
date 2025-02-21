#a
for i in range(101):
    print(i,end=" ")
    
print("\n")
 #b
for i in range(101):
    if(i%7==0):
        print(i,end=" ")
        
print("\n")       

#c
for i in range(101):
    if(i%5==0 and i%3!=0):
        print(i,end=" ")
print('\n')
#d
x= int(input("enter a number: "))
for i in range(2,x):
    if(x%i == 0):
        print(i,end=" ")