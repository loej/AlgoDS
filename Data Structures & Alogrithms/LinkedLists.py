# Linked List implementation:

# 1. Create Node class which instantiates the data and next objects
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def addNode(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        print(newNode.data)

    def reverseLL(self):
        prev = None 
        curr = self.head
        while(curr is not None):
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next 
        self.head = prev
    
    def locateNode(self, x):
        curr = self.head 
        while (curr is not None):
            if (curr.data == x): 
                print('The item you want is: ' + str(x))
                break
            else:
                print('The item is not found.')
            curr = curr.next 

    def insertNode(self, nodeBefore, nodeAfter, item):
        curr = self.head
        if curr is None: return f'There are no inserts.'
        while (curr is not None):
            if curr.data == nodeBefore and curr.next == nodeAfter:
                newNode = Node(item)
                nodeBefore.next = newNode
                newNode.next = nodeAfter
            curr = curr.next

def main():
    # Create LL object 
    LOne = LinkedList()
    # LOne.head = Node('Program: 1')
    # Has to add pointer first 
    # print(LOne.head.data)
    for i in range(0,10):
        LOne.addNode(i)
    LOne.locateNode(1)
    LTwo = Node('twenty')

    LOne.next = LTwo
    LOne.reverseLL()
    
        


if __name__=="__main__":
    main()