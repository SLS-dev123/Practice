a = [1,2,3,4,5,6,7,8,9]
b= a
c= a[:]
b[1] = "orange"
c[2] = "banana"
print(a)
def set_first_element_to_zero(x):
    x[0] = "0"
    return x
set_first_element_to_zero(a)
print(a)