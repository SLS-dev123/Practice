import random
#a
def write(a,b,n):
    list = []
    while n > 0:
        num = random.randint(a,b)
        list.append(num)
        n -= 1
    with open('filename.txt','w') as file:
        for item in list:
               file.write(str(item))
    file.close()
#b
def read():
    with open('filename.txt','r') as file:
        content = file.read()
    file.close()
    return content 
#c
def write2(a,b,n):
    list2 = []
    while n > 0:
        num = random.randint(a,b)
        list2.append(num)
        n -= 1
    with open('filename2','w') as file2:
        for item in list2:
            file2.write(str(item))
    file2.close()
def readandcheck(k):
    with open("filename.txt",'r') as file1:
        content1 = file1.read()
        list(content1)
        list1 = list(map(int,content1))
    file1.close()
    with open("filename2.txt",'r') as file2:
        content2 = file2.read()
        list(content2)
        list2 = list(map(int,content2))
    file2.close()
    result = []
    for item in list1:
        for value in list2:
            if item + value == k:
                result.append(item,value)
    print(result)
       
a = int(input("enter an interger: "))
n = int(input("enter the number of numbers you want in the list: "))
b = int(input(f"enter number biger than {a} + {n}: "))
k = int(input("enter the value of k: "))
write(a,b,n)
read()
write2(a,b,n)
readandcheck(k)