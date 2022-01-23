class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, data):
        self.root = Node(data)
    
    def print(self, type):
        if type == "preorder":
            return self.preorder(self.root).rstrip("-")
        elif type == "inorder":
            return self.inorder(self.root).rstrip("-")
        elif type == "postorder":
            return self.postorder(self.root).rstrip("-")
        else:
            return "Not found"
    
    def preorder(self, node, output = ""):
        if node:
            output += str(node.data) + "-"
            output = self.preorder(node.left, output)
            output = self.preorder(node.right, output)
        return output

    def inorder(self, node, output = ""):
        if node.left:
            output = self.inorder(node.left, output)
        output += str(node.data) + "-"
        if node.right:
            output = self.inorder(node.right, output)
        return output
    
    def postorder(self, node, output = ""):
        if node:
            output = self.postorder(node.left, output)
            output = self.postorder(node.right, output)
            output += str(node.data) + "-"
        return output
