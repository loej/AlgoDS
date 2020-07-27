# Linked List implementation:

# 1. Create Node class which instantiates the data and next objects

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def loopLL(self):
        ptr = self.head 
        while ptr:
            print(ptr.data)
            ptr = ptr.next

    def reverseLL(self):
       pass



        
def main():
    LLOne = LinkedList()
    LLOne.head = Node(3)
    LLtwo = Node(5)
    LLThree = Node(7)

    LLOne.head.next = LLtwo
    LLtwo.next = LLThree
    LLOne.loopLL()

if __name__=='__main__':
    main()