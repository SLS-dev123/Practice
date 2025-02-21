def is_prime(num):
    isprime = True
    for i in range(2,num):
        if(num%i == 0):
            isprime = False
            break
    if(isprime):
        print("True")
num = int(input("enter a number: "))
print(is_prime(num))