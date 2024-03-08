#include "Stack.h"

int main() {
    Stack<int> stack;

    stack.push(33);
    stack.push(44);
    stack.push(55);

    std::cout << "First stack print" << std::endl;
    stack.printStack();

    stack.pop();
    
    std::cout << "Second stack print" << std::endl;
    stack.printStack();

    return 0;
}