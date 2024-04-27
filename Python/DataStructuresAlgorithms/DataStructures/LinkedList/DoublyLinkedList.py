from ..utils.CustomException import EmptyList

class Node:
        """
        Each element in the linked list will be of Node type with three properties:
            data -> the data being stored in the list
            next -> the next element in the list
            previous -> the previous element in the list
        """
        def __init__(self, data, next=None, previous=None):
            self.data = data
            self.next = next
            self.previous = previous

class DoublyLinkedList:
    """
    A Doubly Linked List
    Each node has three properties:
        size_ -> the number of nodes in the linked list
        head_ -> the first element in the list, used as the entry point for the front of the list
        tail_ -> the last element in the list, used as entry point for the back of the list
    """

    def __init__(self):
        """When list is constructed set size to zero and the head and tail node to None"""
        self.size_ = 0
        self.head_ = None
        self.tail_ = None

    def size(self):
        """Helper method to return the size of the list"""
        return self.size_
    
    def is_empty(self):
        """Helper method to check if list is empty"""
        return self.head_ is None
    
    def peak_front(self):
        """Returns the data in the head node"""
        if self.head_ is not None:
            return self.head_.data
        else:
            raise EmptyList('peak_front() called on empty list')
        
    def peak_back(self):
        """Returns the data in the tail node"""
        if self.tail_ is not None:
            return self.tail_.data
        else:
            raise EmptyList('peak_back() called on empty list')

    def push_front(self, data):
        """Adds a new node with data to the head of the list"""
        node = Node(data)

        if self.head_ is None:
            self.head_ = node
            self.tail_ = node
        else:
            current_head = self.head_
            node.previous = node
            node.next = current_head
            self.head_ = node
        
        self.size_ += 1

    def push_back(self, data):
        """Adds a new node with data to the tail of the list"""
        node = Node(data)

        if self.tail_ is None:
            self.tail_ = node
            self.head_ = node
        else:
            current_tail = self.tail_
            current_tail.next = node
            node.previous = current_tail
            self.tail_ = node
        
        self.size_ += 1

    def pop_front(self):
        """Removes head node and sets 2nd node as the new head node"""
        if self.head_ is None:
            # make sure a stray tail pointer is not left
            self.tail_ = None
            return None
        
        if self.head_.next is None:
            self.head_ = None
            self.tail_ = None
            self.size_ -= 1
            return None
        
        self.head_ = self.head_.next
        self.size_ -= 1
        return None
    
    def pop_back(self):
        """Removes tail node and sets 2nd to last node as the new tail node"""
        if self.tail_ is None:
            # make sure a stray head pointer is not left
            self.head_ = None
            return None
        
        if self.tail_.previous is None:
            self.head_ = None
            self.tail_ = None
            self.size_ -= 1
            return None
        
        self.tail_ = self.tail_.previous
        self.tail_.next = None
        self.size_ -= 1
        return None

    def clear(self):
        """Helper method to clear all nodes from a list"""
        while self.head_ is not None:
            self.pop_front()

        # make sure both head and tail pointers are cleared out
        self.head_ = None
        self.tail = None

    # Traversals
    def exists(self, data_to_find):
        """Traverse list to check if data_to_find exists as any node's data in the list"""
        current_node = self.head_

        while(current_node is not None):
            if (current_node.data == data_to_find):
                return True
    
            current_node = current_node.next
        
        return False

    def print_list_forward(self):
        """Helper method for printing out each node's data"""
        current_node = self.head_

        while(current_node is not None):
            print('Node->', current_node.data, end=" ")
            current_node = current_node.next
        print('')

    def print_list_backward(self):
        """Helper method for printing out each node's data in reverse"""
        current_node = self.tail_

        while(current_node is not None):
            print('Node->', current_node.data, end=" ")
            current_node = current_node.previous
        print('')

    
    