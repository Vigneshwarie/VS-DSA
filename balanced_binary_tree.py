# Given a binary tree, determine if it is height-balanced.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Recursive Approach

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: TreeNode):
    def height(node: TreeNode):
        if node is None:
            return -1

        leftHeight = height(node.left)
        rightHeight = height(node.right)

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

# Bottom-Up Approach


def isBalancedBottomUp(root: TreeNode):
    def checkBalance(node: TreeNode):
        if node is None:
            return -1, True

        leftHeight, leftBalanced = checkBalance(node.left)
        rightHeight, rightBalanced = checkBalance(node.right)

        if not leftBalanced or not rightBalanced:
            return 0, False

        if abs(leftHeight - rightHeight) > 1:
            return 0, False

        return max(leftHeight, rightHeight)+1, True

    _, balanced = checkBalance(root)

    return balanced


mytree = TreeNode(1)
mytree.left = TreeNode(2)
mytree.right = TreeNode(2)
mytree.left.left = TreeNode(3)
mytree.left.right = TreeNode(4)
mytree.right.left = TreeNode(4)
mytree.right.right = TreeNode(3)
print(isBalancedBottomUp(mytree))
