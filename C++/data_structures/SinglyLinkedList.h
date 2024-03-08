#pragma once

#include <stdexcept>
#include <iostream>


template <typename T>
class LinkedList {
    public:

    // inner node class
    class Node {
        public:
            Node* next;
            T data;

            // Constructor
            Node(const T& newData) : next(nullptr), data(newData) {}

            // Copy Constructor
            Node(const Node& other) : next(other.next), data(other.data) {}

            // Copy Assignment Operator
            Node& operator=(const Node& other) {
                next = other.next;
                data = other.data;
                return *this;
            }

            // Destructor
            ~Node() {}
        };

    private:
        Node* head_;
        int size_ = 0;

    public:
        int size() const { return size_; }
        int empty() const { return !head_; }

        T peak();
        void push(const T& newData);
        void pop();
        void clear();

        // traversals
        bool exists(const T& dataToFind);
        void printList();

        // Destructor
        ~LinkedList() {
            clear();
        }
};

// Implementation

template <typename T>
void LinkedList<T>::clear() {
    while(head_) {
        pop();
    }
}

template<typename T>
T LinkedList<T>::peak() {
    if (head_) {
        return head_->data;
    } else {
        throw std::runtime_error("peakFront() called on empty list");
    }
}

template<typename T>
void LinkedList<T>::push(const T& newData) {
    Node* newNode = new Node(newData);

    if (!head_) {
        head_ = newNode;
    } else {
        Node* currHead = head_;
        newNode->next = currHead;
        head_ = newNode;
    }

    size_++;
}

template<typename T>
void LinkedList<T>::pop() {
    if (!head_) { return; }

    if (!head_->next) {
        delete head_;

        head_ = nullptr;
        size_--;

        return;
    }

    Node* currHead = head_;
    head_ = head_->next;

    delete currHead;
    currHead = nullptr;
    size_--;
}

// TODO traversals
template<typename T>
bool LinkedList<T>::exists(const T& dataToFind) {
    Node* curr = head_;
    
    while (curr) {
        if(curr->data == dataToFind) {
            return true;
        }

        curr = curr->next;
    }

    return false;
}

template<typename T>
void LinkedList<T>::printList() {
    Node* curr = head_;
    
    while (curr) {
        std::cout << "Node: " << curr->data << std::endl; 

        curr = curr->next;
    }
}
