from ..data_structures.binary_tree import Node, BinaryTree

'''
      1
     / \
    2  3
  /\   /\
 4  5  6 7


'''

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.right.left = Node(5)
tree.root.right.right = Node(6)
tree.root.right.left.left = Node(7)
tree.root.right.left.right = Node(8)


print(tree.print("inorder"))
print(tree.print("preorder"))
print(tree.print("postorder"))