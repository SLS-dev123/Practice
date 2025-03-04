list1 = []
for i in range(101):
    list1.append(i)
evennumbers = list(filter(lambda x: x%2 ==0,list1))
print(evennumbers)