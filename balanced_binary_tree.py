# Given a binary tree, determine if it is height-balanced.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Recursive Approach

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode):
    def height(root: TreeNode):
        if root is None:
            return -1

        leftHeight = height(root.left)
        rightHeight = height(root.right)

        if abs(leftHeight - rightHeight) > 1 or leftHeight == -2 or rightHeight == -2:
            return -2
        else:
            return max(leftHeight, rightHeight) + 1

    return height(root) != -2


mytree = TreeNode(1)
mytree.left = TreeNode(2)
mytree.right = TreeNode(2)
mytree.left.left = TreeNode(3)
mytree.left.right = TreeNode(4)
mytree.left.left.left = TreeNode(4)
mytree.left.right.right = TreeNode(3)
print(isBalanced(mytree))
