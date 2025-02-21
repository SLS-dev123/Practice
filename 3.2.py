from math import sqrt
def polynomial(a,b,c):
    D = b*b-4*a*c
    if(D == 0):
        print("the roots are real and equal!")
        ans = -b/(2*a)
        print("the answer is: ",ans)
    elif(D > 0):
        print("the roots are real and distinct!")
        q = sqrt(D)
        ans1 = (-b+q)/(2*a)
        ans2 = (-b-q)/(2*a)
        print(f"x1 = {ans1} and ans2 = {ans2}")
    else:
        print("the roots are complex!")
        q = sqrt(-D)
        p = -b/(2*a)
        print(f"the answers are ans1 = {p}+{q}i and ans2 ={p}-{q}i")
print("this solves a quadratic equation of the form ax^2 + bx + c")
a = int(input("enter the value of a: "))
b = int(input("enter the value of b: "))
c = int(input("enter the value of b: ")) 
polynomial(a,b,c)   
    