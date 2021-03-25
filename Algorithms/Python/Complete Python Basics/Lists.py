# A value that contains a value in an ordered sequence
sampleList = ['apple', 'pizza', 'chicken']
print(sampleList)
# You only access the values in the list 
for i in sampleList:
    print(i)

doubleList = [[0, 1, 2, 3], ["hello", "world", ["hi", "vscode"]]]
for index in doubleList:
    for index2 in index:
        print(index2)
        # for index3 in index2:
        #     print(index3)

# Replaces the sampleList values 
sampleList[0:2] = ['hello', 'world']
print(sampleList)

# Manipulating Lists

text = "hello"
foo1 = text*3
print(foo1)

# Concatnates lists
zen = ['sample','ok'] + [1,2,3]
print(zen)

# Returns a list form of whatever is passed
# Seperates every single value inside the string
zen1 = list('hi')
print(zen1)

# Evaluates to True
list3 = ['cat', 'dog']

foo3 = 'cat' in list3
print(foo3)

# Final slicing example
finalList = [111 , 112 , 205, 206, 336]
finalList = finalList[:3]
print(finalList)
