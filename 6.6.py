def find(value,dictionary):
    return dictionary.get(value)
value = eval(input("enter a letter between a and k: "))
dictionary = dict(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10,k=11)
result = find(value,dictionary)
print(result)