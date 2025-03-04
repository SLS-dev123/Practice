list1 = []
for i in range(2,101):list1.append(i)
isprime = lambda n: n>1 and all(n%i for i in range(2, int(n**0.5)+1))
primenumbers = list(filter(isprime,list1))
print(primenumbers)