sentence = eval(input("enter a sentence 'in quotes': ")).split(" ")
longest = ""
for word in sentence:
    if len(word) > len(longest):
        longest = word
print(longest)