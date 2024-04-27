class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self, root_node=None):
        # point to root node of the tree
        self.root_node = root_node

    def insert(self, node, data):
        # if tree is empty, return new node
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        # return inserted node
        return node
    
    def search(self, data):
        if self.root_node is None or self.root_data.data == data:
            return self.root_node
        
        if self.root_node.data < data:
            return self.search(self.root_node, data)
        
        return self.search(self.root_node, data)

    def remove(self, data):
        pass

    def inorder_traversal(self):
        pass