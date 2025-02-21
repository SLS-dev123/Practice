def my_max(x,y):
    if(x > y):
        print("the greater number is ",x)
    if(y > x):
        print("the greater number is ",y)
    if(x == y):
        print("they are equal!")
print("enter two numbers")
x = int(input("enter the first number: ")) 
y = int(input("enter the second number: "))
print(my_max(x,y))