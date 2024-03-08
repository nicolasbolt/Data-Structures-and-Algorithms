#pragma once

#include <stdexcept>
#include "DoublyLinkedList.h"

template <typename T>
class Stack {
    private:
        LinkedList<T> list_;

    public:
        T pop();
        void push(const T& newData);
        int size();
        void printStack();
};

template<typename T>
T Stack<T>::pop() {
    if (size() == 0) {
        throw std::runtime_error("pop() called on empty Stack");
    }
    
    T value = list_.peakBack();
    list_.popBack();

    return value;
}

template<typename T>
void Stack<T>::push(const T& newData) {
    list_.pushFront(newData);
}

template<typename T>
int Stack<T>::size() {
    return list_.size();
}

template<typename T>
void Stack<T>::printStack() {
    list_.printListForward();
}