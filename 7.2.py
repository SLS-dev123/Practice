#a
with open('new.txt','r') as file:  
    content = file.read()
    words = content.split()
file.close()
#print(words)
def count(words):
    store = dict()
    for word in words:
        store[word] = store.get(word,0) + 1
    return  store
def arrange(store):
    return dict(sorted(store.items(), key = lambda item : item[1], reverse =True))
def sort(store):
    sorted_items = sorted(store.items(), key= lambda item: item[1], reverse = True )
    for i,(key,value) in enumerate(sorted_items[:20]):
        print(f"key: {key}, value: {value} ")
        if i == 19:
            break
    #print(sorted_items)
var = count(words)
ans = arrange(var)
sort(ans)