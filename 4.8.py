def join(list1):
    length = len(list1)
    newlist = []
    for i in range(length):
        newlist += list1[i]
    print(newlist)

list1=[[1,2,3],[4,5,6],[7,8,9]]
join(list1)