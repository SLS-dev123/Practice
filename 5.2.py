x = [1,2,3,4,5,6,7,8,9]
y = [9,8,7,6,5,4,3,2,1]
zipped = zip(x,y)
print(list(zipped))
unzipped = zip(*zipped)
print(list(unzipped))
unzippedx = list(unzipped[0])
unzippedy = list(unzipped[1])
print(unzippedx)
print(unzippedy)