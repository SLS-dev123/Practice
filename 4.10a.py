def collattz_seq(n):
    sequence = [n]
    while n != 1:
        if n%2 != 0:
            n = n//2
        else:
            n = 3*n+1
        sequence.append(n)
    print(sequence)
n = int(input("Enter the value of n: "))
collattz = collattz_seq(n)