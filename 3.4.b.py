def is_prime(num):
    if(num == 2 or num == -2):
        print("True")
    if(num == 3 or num == -3):
        print("True")
    for k in range(2,num):
        B1 = 6*k+1
        B2 = 6*k-1
        if(B1 == num or B2 == num):
            print("True")
num = int(input("enter a number: "))
print(is_prime(num))