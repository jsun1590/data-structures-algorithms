class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    
    def print_tree(self, type):
        if type == "preorder":
            return self.preorder(self.root).rstrip("-")
        elif type == "inorder":
            return self.inorder(self.root).rstrip("-")
    
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



'''
         1
       /   \
      2     3
     / \   /  \
    4   5 6    7
'''

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("inorder"))