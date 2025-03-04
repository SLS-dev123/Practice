#longest collatz sequence
def collattz_seq(n):
    sequence = [n]
    while n != 1:
        if n%2 != 0:
            n = n//2
        else:
            n = 3*n+1
        sequence.append(n)
    return sequence        

def longest_seq(x,y,z):
    i = collattz_seq(x)
    j = collattz_seq(y)
    k = collattz_seq(z)
    print(i,k,j)
    if len(i) > len(j) and len(i) > len(k):
        longest = x
    elif len(j) > len(i) and len(j) > len(k):
        longest = y
    else:
        longest = z
    return longest 
    
x = int(input("Enter the first number: "))
y = int(input("Enter the second nummber: "))
z = int(input("Enter the third number: "))
ans = longest_seq(x,y,z)
print(ans)