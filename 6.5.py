import numpy as np
vector1 = np.array([1.0,3.4,2.4,5.8,4.5]) #dense vector
vector2 = np.array([1.0,1.2,1.3,1.4,1.5]) # dense vector
vector3 = {2:1,2:3,2:5,2:6,2:7}
vector4 = {1:1,2:3,2:5,4:6,3:7}
#a
def sumdense(a,b):
    result = a+b
    print(result)
#b 
def multiplydense(a,b):
    result = a*b
    print(result)
#c
def sumsparse(a,b):
    result = {}
    for key in set(a)|set(b):
        result[key] =a.get(key,0) + b.get(key,0)
    print(result)    
#d
def multiplysparse(a,b):
    result = []
    for key in set(a)|set(b):
        result.append(a.get(key,0)*b.get(key,0))
    print(result)
#e
def sumsparsedense(a,b):
    result = []
    for key in set(a):
        result.append(a.get(key,0)+b)
        print(result)
#f
def multiplysparsedense(a,b):
    result = []
    for key in set(a):
        result.append(a.get(key,0)*b)
    print(result)

sumdense(vector1,vector2)
multiplydense(vector1,vector2)
sumsparse(vector3,vector4)
multiplysparse(vector3,vector4)
sumsparsedense(vector3,vector1)
multiplysparsedense(vector4,vector2)