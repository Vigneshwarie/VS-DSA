# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minimum_depth(root: BinaryTree):
    if root is None:
        return 0

    if root.left is None:
        return minimum_depth(root.right) + 1
    elif root.right is None:
        return minimum_depth(root.left) + 1

    leftHeight = minimum_depth(root.left)
    rightHeight = minimum_depth(root.right)

    return min(leftHeight, rightHeight) + 1


mytree = BinaryTree(1)
mytree.left = BinaryTree(2)
mytree.right = BinaryTree(3)
mytree.left.left = BinaryTree(4)
mytree.left.right = BinaryTree(5)
# mytree.right.right = BinaryTree(6)
mytree.left.left.left = BinaryTree(7)
mytree.left.left.right = BinaryTree(8)


output = minimum_depth(mytree)
print(output)
