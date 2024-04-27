from DataStructuresAlgorithms.DataStructures.LinkedList.SinglyLinkedList import SinglyLinkedList
from DataStructuresAlgorithms.DataStructures.LinkedList.DoublyLinkedList import DoublyLinkedList
from DataStructuresAlgorithms.DataStructures.Queue import Queue
from DataStructuresAlgorithms.DataStructures.Stack import Stack

"""This file contains example functions to use the different data structures created in this project"""

def main():
    # run SinglyLinkedList implementation example
    # singly_linked_list_example()

    # run DoublyLinkedList implementation example
    # doubly_linked_list_example()

    # run queue implementation example
    # queue_example()

    # run stack implementation example
    stack_example()


def singly_linked_list_example():
    print('Testing SinglyLinkedList...')
    linked_list = SinglyLinkedList()
    # to test exception
    # linked_list.peak()

    print('is_empty: ', linked_list.is_empty())
    linked_list.push(5)
    linked_list.print_list()
    linked_list.push(77)
    linked_list.print_list()
    print('size ', linked_list.size())
    print('peak: ', linked_list.peak())
    linked_list.pop()
    print('5 exists: ', linked_list.exists(5))
    print('77 exists: ', linked_list.exists(77))
    linked_list.clear()
    print('size: ', linked_list.size())

def doubly_linked_list_example():
    print('Testing DoublyLinkedList...')
    linked_list = DoublyLinkedList()

    # to test exception
    # linked_list.peak_back()
    # linked_list.peak_front()

    print('Testing front functions...\n')
    print('is_empty: ', linked_list.is_empty())
    linked_list.push_front(5)
    linked_list.print_list_forward()
    linked_list.push_front(77)
    linked_list.print_list_forward()
    print('size ', linked_list.size())
    print('peak_front: ', linked_list.peak_front())
    linked_list.pop_front()
    print('5 exists: ', linked_list.exists(5))
    print('77 exists: ', linked_list.exists(77))

    print('clearing list...')
    linked_list.clear()
    print('size: ', linked_list.size())
    print('head pointer: ', linked_list.head_)
    print('tail pointer: ', linked_list.tail_)

    print('Testing back functions...\n')
    linked_list.push_back(5)
    linked_list.push_back(77)
    linked_list.print_list_backward()
    print('size before pop_back: ', linked_list.size())
    linked_list.pop_back()
    print('size after pop_back: ', linked_list.size())
    linked_list.print_list_backward()

    print('clearing list...')
    linked_list.clear()
    print('size: ', linked_list.size())
    print('head pointer: ', linked_list.head_)
    print('tail pointer: ', linked_list.tail_)

def queue_example():
    print('Testing Queue...')
    queue = Queue()

    # to test exception
    # queue.dequeue()

    queue.enqueue(5)
    queue.enqueue(77)
    print('size: ', queue.size())
    queue.print_queue()
    print('deqeued value: ', queue.dequeue())
    print('size: ', queue.size())
    queue.print_queue()
    print('dequeued value: ', queue.dequeue())
    print('size: ', queue.size())

    queue.enqueue(65)
    queue.enqueue(767)
    queue.enqueue(99)
    print('size: ', queue.size())
    queue.print_queue()
    print('deqeued value: ', queue.dequeue())
    print('size: ', queue.size())
    queue.print_queue()
    print('dequeued value: ', queue.dequeue())
    print('size: ', queue.size())
    queue.print_queue()

def stack_example():
    print('Testing Stack...')
    stack = Stack()

    # to test exception
    # stack.pop()

    stack.push(5)
    stack.push(77)
    print('size: ', stack.size())
    stack.print_stack()
    print('popped value: ', stack.pop())
    print('size: ', stack.size())
    stack.print_stack()
    print('popped value: ', stack.pop())
    print('size: ', stack.size())

    stack.push(65)
    stack.push(767)
    stack.push(99)
    print('size: ', stack.size())
    stack.print_stack()
    print('popped value: ', stack.pop())
    print('size: ', stack.size())
    stack.print_stack()
    print('popped value: ', stack.pop())
    print('size: ', stack.size())
    stack.print_stack()

if __name__ == '__main__':
    main()