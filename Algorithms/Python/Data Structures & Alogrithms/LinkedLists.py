#!/usr/bin/python3 

# Linked List implementation:

# 1. Create Node class which instantiates the data and next objects
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def makeNewNode(self, insert):
        new_node = Node(insert)
        new_node = self.head
        self.head = new_node
        print(new_node.data)
    
    def reverseLL(self):
        prev = None 
        curr = self.head 
        while curr is not None:
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        self.head = prev
    
    def printLL(self):
        curr = self.head 
        if curr is None:
            print('The Linked List is Empty')
        while curr is not None:
            print(curr.data)
            curr = curr.next 



def main():
    link = LinkedList()    
    link.makeNewNode(10)
        


if __name__=="__main__":
    main()