#!/usr/bin/python3 

# Hashtables in Python using dictionaries. 
# Using hash values

country_state = {'USA':'CA', 'CANADA':'QU', 'INDIA' : 'NEPAL'}
hashTable = [None] * 9
# 0 - m-1 
print(hashTable)

# Conventional hasfunction
def hashFunction(item):
    # Use MOD
    return item%len(hashTable)

print(hashFunction(10))
print(hashFunction(90))
print(hashFunction(288282))

# Inserting the data into a the hastable 

def insertItem(hashTable, item, value):
    hashKey = hashFunction(item)
    hashTable[hashKey] = value

insertItem(hashTable,10, 'CA')
print(hashTable)