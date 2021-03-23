class Node:
     def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, newNodeInput):
        newNode = newNodeInput
        if (self.head == None):
            self.head = newNode
        lastNode = self.head
        while (lastNode.next):
            lastNode = lastNode.next
        lastNode.next = newNode

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

