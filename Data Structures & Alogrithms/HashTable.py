# Hashtables in Python using dictionaries. 
# Using hash values

# We are going to use the abstract data type of Map()

class HashTable:

    def __init__(self):
        # Size of the table 0 - 10 
        self.size = 11
        # Size fo the slots 0 - 10 * [ None ]
        self.slots = self.size * [None]
        self.data = self.size * [None]

    def put(self, key, data):
        # hashfunction simply implements a remainder function
        hasvalue = self.hashfunction(key, len(self.slots))
        