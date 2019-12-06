from Empty import Empty
from Outbound import Outbound

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = Node()  # dummy node
        self._length = 0

    def get_first(self):  # get the node, not only the stored value
        if not self.head.next:
            raise Empty('LinkedList is empty')
        return self.head.next
    
    def get_last(self):
        if not self.head.next:
            raise Empty('LinkedList is empty')
        node = self.head
        while not node.next:
            node = node.next
        return node

    def get(self, index):
        if index < 0 or index > self.length:
            raise Outbound('Index is out of bound')
        if not self.head.next:
            raise Empty('LinkedList is empty')
        node = self.head
        for _ in range(index):
            node = node.next
        return node.next


    def add_first(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self._length += 1
        
    def add_last(self, value):
        new_node = Node(value)
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new_node
        self._length += 1
        
    def add(self, value, index):
        if not self.head.next:
            raise Empty('LinkedList is empty')
        if index > self._length or index < 0:
            raise Outbound('Index is out of bound')
        node = self.head
        new_node = Node(value)
        for _ in range(index):
            node = node.next
        new_node.next = node.next
        node.next = new_node
        self._length += 1
    
    def remove_at(self, index):
        if not self.head.next:
            raise Empty('LinkedList is empty')
        if index < 0 or index > self._length:
            raise Outbound('Index is out of bound')
        node = self.head
        for _ in range(index):
            node = node.next
        value = node.next.value
        node.next = node.next.next
        self._length -= 1
        return value
            
    def remove_first(self):
        if not self.head.next:
            raise Empty('LinkedList is empty')
        value = self.head.next.value
        self.head.next = self.head.next.next
        self._length -= 1
        return value
    
    def remove_last(self):
        if not self.head.next:
            raise Empty('LinkedList is empty')        
        prev = self.head
        node = self.head.next
        while not node.next:  # node.next != None
            prev = node
            node = node.next
        prev.next = None
        self._length -= 1
        return node.value           
        
    def print_list(self):
        node = self.head
        while node.next != None:
            node = node.next
            print(node.value, end=' ')
        print('')
        
    def length(self):
        return self._length
    
    