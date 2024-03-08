#include "Queue.h"

int main() {
    Queue<int> queue;

    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);

    std::cout << "First queue print" << std::endl;
    queue.printQueue();

    queue.dequeue();
    queue.dequeue();

    std::cout << "Second queue print" << std::endl;
    queue.printQueue();
    return 0;
}