#counting
def count(list1):
    ans = dict()
    for i in list1:
        ans[i] = ans.get(i,0)+1
    return ans
list1 = [1,2,3,2,1,2,3,4,3,2,1,2,3,4,2]
result = count(list1)
print(result)     
            