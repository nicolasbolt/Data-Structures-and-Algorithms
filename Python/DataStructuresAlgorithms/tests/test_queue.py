import unittest
from DataStructures.Queue import Queue
from DataStructures.LinkedList.DoublyLinkedList import DoublyLinkedList, Node

class TestQueue(unittest.TestCase):

    def test_create_queue(self):
        queue = Queue()
        self.assertTrue(type(queue.list_) == DoublyLinkedList)
    
    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(5)
        self.assertEqual(queue.list_.tail_.data, 5)

    def test_dequeue(self):
        queue = Queue()
        node = Node(5)
        queue.list_.head_ = node
        queue.list_.tail_ = node
        queue.list_.size_ = 1
        actual_value = queue.dequeue()
        self.assertEqual(actual_value, 5)

    def test_size(self):
        queue = Queue()
        node = Node(5)
        queue.list_.head_ = node
        queue.list_.tail_ = node
        queue.list_.size_ = 1
        self.assertEqual(queue.size(), 1)