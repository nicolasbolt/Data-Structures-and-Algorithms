from .LinkedList.DoublyLinkedList import DoublyLinkedList
from .utils.CustomException import EmptyQueue

class Queue:
    """A Queue to handle FIFO operations"""

    def __init__(self):
        """A doubly linked list is used to handle the logic for the queue"""
        self.list_ = DoublyLinkedList()
    
    def dequeue(self):
        """dequeue the next item from the front, if no item exists, raise an EmptyQueue exception"""
        if self.size() == 0:
            raise EmptyQueue('dequeue() called on empty queue')
        
        self.list_.print_list_forward
        value = self.list_.peak_front()
        self.list_.pop_front()

        return value

    def enqueue(self, value):
        """enqueue to the back of the queue"""
        self.list_.push_back(value)

    def size(self):
        return self.list_.size()

    def print_queue(self):
        self.list_.print_list_forward()