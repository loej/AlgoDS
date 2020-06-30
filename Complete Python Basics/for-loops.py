# [Automate the Boring Stuff with Python - Al Sweigart](http://automatetheboringstuff.com/)
# Under the same creative commons license: https://creativecommons.org/licenses/by-nc-sa/3.0/
import time
# Prints Hi 5 times, starts at 0 and advances from there. i always begins at 0.
print('My Hi is:')
for i in range(5):
    print('Hi' + ' ' + str(i))
# Prints the length of Hello
str = "hello"
for j in range(len(str)):
    print(j)

# Prints the contents of a string
str1 = "A very very very very very very long length"
for z in str1:
    print(z)

# Defines the difference between break and continue

# Break completely stops the iteration at that point
list = ["Iteration 1","Iteration 2","Iteration 3","Iteration 4"]
for i in list:
    if i == "Iteration 3":
        break
    print(i)

# Continue skips over the iteration
list = ["Iteration a","Iteration b","Iteration c","Iteration d"]
for c in list:
    if c == "Iteration c":
        continue
    print(c)
# Breaks after it checks for the Iteration
list = ["Iteration aa","Iteration bb","Iteration cc","Iteration dd"]
for h in list:
    print(h)
    if h == "Iteration bb":
         break
# Continues after it checks for the Iteration
list = ["Iteration aaa","Iteration bbb","Iteration ccc","Iteration ddd"]
for h in list:
    print(h)
    if h == "Iteration aaa":
        break
