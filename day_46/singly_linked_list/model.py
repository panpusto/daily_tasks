# implementation of singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def insert(self, data, position):
        data = Node(data)
        count = 1
        current = self.head
        if position == 1:
            data.next = self.head
            self.head = data
        while current:
            if count + 1 == position:
                data.next = current.next
                current.next = data
                return
            else:
                count += 1
                current = current.next
        raise IndexError('Invalid position for insertion.')

    def remove(self, data):
        current = self.head
        if current.data == data:
            self.head = current.next
        else:
            while current:
                if current.data == data:
                    break
                prev = current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
