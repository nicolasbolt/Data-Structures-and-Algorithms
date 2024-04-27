from .LinkedList.SinglyLinkedList import SinglyLinkedList
from .utils.CustomException import EmptyStack

class Stack:
    """A Stack to handle LIFO operations"""

    def __init__(self):
        """A singly linked list is used to handle the logic for the stack"""
        self.list_ = SinglyLinkedList()
    
    def pop(self):
        """push the next item from the front, if no item exists, raise an EmptyStack exception"""
        if self.size() == 0:
            raise EmptyStack('pop() called on empty stack')
        
        value = self.list_.peak()
        self.list_.pop()

        return value

    def push(self, value):
        """push to the front of the stack"""
        self.list_.push(value)

    def size(self):
        return self.list_.size()

    def print_stack(self):
        self.list_.print_list()