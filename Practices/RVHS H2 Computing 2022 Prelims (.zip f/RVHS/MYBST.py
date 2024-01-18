class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        else:
            curr = self.root
            while curr:
                if curr.data > data:
                    if curr.left == None:
                        curr.left = new_node
                        return
                    else:
                        curr = curr.left
                else:
                    if curr.right == None:
                        curr.right = new_node
                        return
                    else:
                        curr = curr.right

    def search(self, data):
        curr = self.root
        while curr:
            if curr.data < data:
                curr = curr.right
            elif curr.data > data:
                curr = curr.left
            else:
                return True
        return False

    def size(self):
        def helper(node):
            if node:
                return 1 + helper(node.left) + helper(node.right)
            else:
                return 0
        return helper(self.root)

    def height(self):
        def helper(node):
            if node:
                lst = helper(node.left)
                rst = helper(node.right)
                return 1 + lst if lst > rst else rst + 1
            else:
                return -1
        return helper(self.root)
                        
    def preorder(self):
        results = ""
        def helper(node):
            nonlocal results
            if node:
                results += str(node.data)
                helper(node.left)
                helper(node.right)
        helper(self.root)
        return results

    def postorder(self):
        results = ""
        def helper(node):
            nonlocal results
            if node:
                helper(node.left)
                helper(node.right)
                results += str(node.data)
        helper(self.root)
        return results
                        
    def preorder(self):
        results = ""
        def helper(node):
            nonlocal results
            if node:
                results += str(node.data)
                helper(node.left)
                helper(node.right)
        helper(self.root)
        return results

    def inorder(self):
        results = ""
        def helper(node):
            nonlocal results
            if node:
                helper(node.left)
                results += str(node.data)
                helper(node.right)
        helper(self.root)
        return results                        
            
