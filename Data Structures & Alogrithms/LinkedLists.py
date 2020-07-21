# Linked List implementation:

# 1. Create Node class which instantiates the data and next objects

class Node:

    def __init__(self, data):
       self.data = data
       self.next = None

class LL:
    
    def __init__(self):
        # Head does not point to anything (yet)
        self.head = None
    
    def printLL(self):
        tempRef = self.head
        while(tempRef):
            print(tempRef.data)
            tempRef = tempRef.next

def main():
    
    # Create LL onject 
    newLL = LL()
    newLL.head = Node('programmer 1')
    secondNode = Node('programmer 2')
    thirdNode = Node('programmer 3')

    newLL.head.next = secondNode
    secondNode.next = thirdNode

    newLL.printLL()


if __name__=='__main__':
    main()