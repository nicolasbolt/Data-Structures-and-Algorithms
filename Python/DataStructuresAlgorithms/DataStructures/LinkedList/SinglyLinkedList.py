from ..utils.CustomException import EmptyList

class Node:
        """
        Each element in the linked list will be of Node type with two properties:
            data -> the data being stored in the list
            next -> the next element in the list
        """
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

class SinglyLinkedList:
    """
    A Singly Linked List
    Each node has two properties:
        size_ -> the number of nodes in the linked list
        head_ -> the first element in the list, used as the entry point for the list
    """

    def __init__(self):
        """When list is constructed set size to zero and the head node to None"""
        self.size_ = 0
        self.head_ = None

    def size(self):
        """Helper method to return the size of the list"""
        return self.size_
    
    def is_empty(self):
        """Helper method to check if list is empty"""
        return self.head_ is None
    
    def peak(self):
        """Returns the data in the head node"""
        if self.head_ is not None:
            return self.head_.data
        else:
            raise EmptyList('peak() called on empty list')

    def push(self, data):
        """Adds a new node with data to the head of the list"""
        node = Node(data)

        if self.head_ is None:
            self.head_ = node
        else:
            current_head = self.head_
            node.next = current_head
            self.head_ = node
        
        self.size_ += 1

    def pop(self):
        """Removes head node and sets 2nd node as the new head node"""
        if self.head_ is None:
            return None
        
        if self.head_.next is None:
            self.head_ = None
            self.size_ -= 1
            return None
        
        self.head_ = self.head_.next
        self.size_ -= 1
        return None

    def clear(self):
        """Helper method to clear all nodes from a list"""
        while self.head_ is not None:
            self.pop()

    # Traversals
    def exists(self, data_to_find):
        """Traverse list to check if data_to_find exists as any node's data in the list"""
        current_node = self.head_

        while(current_node is not None):
            if (current_node.data == data_to_find):
                return True
    
            current_node = current_node.next
        
        return False

    def print_list(self):
        """Helper method for printing out each node's data"""
        current_node = self.head_

        while(current_node is not None):
            print('Node->', current_node.data, end=" ")
            current_node = current_node.next
        print('')

    
    