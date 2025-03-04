def distance(l1,l2):
    list1 = []
    list2 = []
    for i in range(len(l1)):
        sep = l2[0][i]-l1[0][i]
        list1.append(sep)   
    
    for j in range(len(l1)):
        sep = l2[1][j]-l1[1][j]
        list2.append(sep)
    result = zip(list1,list2)
    return result
x1 = [3,5,8,2,5,8,5,7]
y1 = [4,6,5,7,8,2,4,6]
x2 = [1,5,2,6,8,3,6,8]
y2 = [6,1,4,7,3,6,9,23]
l1 = tuple(zip(x1,y1))
l2 = tuple(zip(x2,y2))
ans = distance(l1,l2)
print(ans)