#include "SinglyLinkedList.h"

int main() {
    LinkedList<int> list;
    list.push(5);
    list.push(45);
    list.push(33);

    list.printList();

    list.pop();

    list.printList();

    std::cout << "Peak: " << list.peak() << std::endl;

    std::cout << "Exists: " << list.exists(45) << std::endl;
    std::cout << "Exists: " << list.exists(111) << std::endl;
    return 0;
}