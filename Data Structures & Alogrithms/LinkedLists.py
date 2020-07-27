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
    
    def locateNode(self, x):
        temp = self.head 
        while (temp is not None):
            if (temp.data == x):
                return temp.data
        temp = temp.next

    def reverseLL(self):
        prev = None 
        curr = self.head 
        while (curr is not None):
           next = curr.next
           curr.next = prev 
           prev = curr
           curr = next
        self.head = prev
      
def main():
    LLOne = LinkedList()
    LLOne.head = Node(3)
    LLtwo = Node(5)
    LLThree = Node(7)
    LLfour = Node('hello')

    LLOne.head.next = LLtwo
    LLtwo.next = LLThree
    LLThree.next = LLfour
    LLOne.loopLL()
    LLOne.reverseLL()
    print('--')
    LLOne.loopLL()
    LLOne.locateNode(3)

if __name__=='__main__':
    main()