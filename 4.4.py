def ask(x,index):
    x[index]= "0"
x= []
count = int(input("how many elements do you want in your list: "))
for i in range(count):
    k= eval(input("enter an element: "))
    x.append(k)
index = int(input("enter the index: "))
ask(x,index)
print(x)