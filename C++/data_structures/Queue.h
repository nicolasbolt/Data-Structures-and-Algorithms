#pragma once

#include <stdexcept>
#include "SinglyLinkedList.h"

template <typename T>
class Queue {
    private:
        LinkedList<T> list_;

    public:
        T dequeue();
        void enqueue(const T& newData);
        int size();
        void printQueue();
};

template<typename T>
T Queue<T>::dequeue() {
    if (size() == 0) {
        throw std::runtime_error("dequeue() called on empty queue");
    }
    
    T value = list_.peak();
    list_.pop();

    return value;
}

template<typename T>
void Queue<T>::enqueue(const T& newData) {
    list_.push(newData);
}

template<typename T>
int Queue<T>::size() {
    return list_.size();
}

template<typename T>
void Queue<T>::printQueue() {
    list_.printList();
}
