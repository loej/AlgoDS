#!/usr/bin/python3 

# Stacks and Queues implementation:

#A Stacka is Last in First Out === LIFO
stack = [] 

for x in range(0,10):
    # Use append function to push
    stack.append(x)

print(stack)

# the indeces in the list will change after every pop, therefore iterating just the list 
# will not necessarily work

for i in range(10):
    temp = stack.pop()
    print(stack)

