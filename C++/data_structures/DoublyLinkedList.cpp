#include "DoublyLinkedList.h"

LinkedList<int> createList() {
    LinkedList<int> list;

    // push an item and check that it was correctly added
    // 15 -> 5 -> 25 -> 10
    list.pushFront(5);
    list.pushFront(15);
    list.pushBack(25);
    list.pushBack(10);

    // Check size
    std::cout << "Size: " << list.size() << std::endl;

    // Check Head
    std::cout << "Head: " << list.peakFront() << std::endl;

    // Check Tail
    std::cout << "Tail: " << list.peakBack() << std::endl;

    list.printListForward();
    list.printListBackward();

    std::cout << "Exists: " << list.exists(5) << std::endl;
    std::cout << "Exists: " << list.exists(6) << std::endl;

    return list;
}

LinkedList<int> updateList(LinkedList<int> list) {
    std::cout << "Head: " << list.peakFront() << std::endl;
    list.popFront();
    std::cout << "Head: " << list.peakFront() << std::endl;

    std::cout << "Tail: " << list.peakBack() << std::endl;
    list.popBack();
    std::cout << "Tail: " << list.peakBack() << std::endl;

    // Check size
    std::cout << "Size: " << list.size() << std::endl;

    return list;
}

int main() {
    LinkedList<int> list = createList();
    updateList(list);

    return 0;
}
