import unittest
from DataStructures.Stack import Stack
from DataStructures.LinkedList.SinglyLinkedList import Node

class StackTest(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(5)
        self.assertTrue(stack.list_.head_.data == 5)

    def test_pop(self):
        stack = Stack()
        stack.list_.head_ = Node(5)
        stack.list_.size_ = 1
        actual_value = stack.pop()
        self.assertTrue(actual_value == 5)

    def test_size(self):
        stack = Stack()
        stack.list_.head_ = Node(5)
        stack.list_.size_ = 1
        self.assertTrue(stack.size() == 1)