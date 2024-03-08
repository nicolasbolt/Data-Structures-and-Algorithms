#pragma once

#include <stdexcept>


template <typename T>
class LinkedList {
    public:

    // inner node class
    class Node {
        public:
            Node* next;
            Node* previous;
            T data;

            // Constructor
            Node(const T& newData) : next(nullptr), previous(nullptr), data(newData) {}

            // Copy Constructor
            Node(const Node& other) : next(other.next), previous(other.previous), data(other.data) {}

            // Copy Assignment Operator
            Node& operator=(const Node& other) {
                next = other.next;
                previous = other.previous;
                data = other.data;
                return *this;
            }

            // Destructor
            ~Node() {}
        };

    private:
        Node* head_;
        Node* tail_;
        int size_ = 0;

    public:
        int size() const { return size_; }
        int empty() const { return !head_; }

        T peakFront();
        T peakBack();
        void pushFront(const T& newData);
        void pushBack(const T& newData);
        void popFront();
        void popBack();
        void clear();

        // traversals
        T find();
        void printListForward();
        void printListBackward();

        // Destructor
        ~LinkedList() {
            clear();
        }
};


// Implementation

template <typename T>
void LinkedList<T>::clear() {
    while(head_) {
        popBack();
    }
}

template<typename T>
T LinkedList<T>::peakFront() {
    if (head_) {
        return head_->data;
    } else {
        throw std::runtime_error("peakFront() called on empty list");
    }
}

template<typename T>
T LinkedList<T>::peakBack() {
    if (tail_) {
        return tail_->data;
    } else {
        throw std::runtime_error("peakBack() called on empty list");
    }
}

template<typename T>
void LinkedList<T>::pushFront(const T& newData) {
    Node* newNode = new Node(newData);

    if (!head_) {
        head_ = newNode;
        tail_ = newNode;
    } else {
        Node* currHead = head_;
        currHead->previous = newNode;
        newNode->next = currHead;
        head_ = newNode;
    }

    size_++;
}

template<typename T>
void LinkedList<T>::pushBack(const T& newData) {
    Node* newNode = new Node(newData);

    if (!tail_) {
        tail_ = newNode;
        head_ = newNode;
    } else {
        Node* currHead = tail_;
        newNode->previous = currHead;
        currHead->next = newNode;
        
        tail_ = newNode;
    }

    size_++;
}

template<typename T>
void LinkedList<T>::popFront() {
    if (!head_) { return; }

    if (!head_->next) {
        delete head_;

        head_ = nullptr;
        tail_ = nullptr;
        size_--;

        return;
    }

    Node* currHead = head_;
    head_ = head_->next;
    head_->previous = nullptr;

    delete currHead;
    currHead = nullptr;
    size_--;
}

template<typename T>
void LinkedList<T>::popBack() {
    if (!tail_) { return; }

    if (!tail_->previous) {
        delete tail_;

        tail_ = nullptr;
        tail_ = nullptr;
        size_--;

        return;
    }

    Node* currTail = tail_;
    tail_ = tail_->previous;
    tail_->next = nullptr;

    delete currTail;
    currTail = nullptr;
    size_--;
}

// TODO traversals
