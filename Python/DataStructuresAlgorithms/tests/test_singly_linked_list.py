import unittest

from DataStructures.LinkedList.SinglyLinkedList import SinglyLinkedList, Node

class TestSinglyLinkedList(unittest.TestCase):

    def test_list_create(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(linked_list.size_, 0)
        self.assertEqual(linked_list.head_, None)

    def test_size(self):
        linked_list = SinglyLinkedList()
        linked_list.size_ = 2
        self.assertEqual(linked_list.size(), 2)