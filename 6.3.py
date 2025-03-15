def function(key_,default):
    list  = []
    found = False
    dictionary = dict(x=1,d=3,m=4,f=5,g=4,t=5,k=7)
    for keys in dictionary:
        if key == keys:
            found = True
    if(found):
        print(dictionary['key_'])
    else:
        print(default)
key = eval(input("enter a key: "))
default = int(input("enter the default value: "))
function(key,default)