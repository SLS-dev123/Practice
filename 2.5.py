number_found = 0
i=0
while number_found <= 20:
    if(i%5==0 and i%7==0 and i%11==0):
        print(i,end = " ")
        number_found+=1
    i+=1