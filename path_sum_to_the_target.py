# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, targetSum: int):
    def helper(node: TreeNode, currentSum: int):
        if node is None:
            return False

        currentSum += node.val

        if node.left is None and node.right is None:
            return targetSum == currentSum

        return helper(node.left, currentSum) or helper(node.right, currentSum)

    return helper(root, 0)


mytree = TreeNode(1)
mytree.left = TreeNode(2)
mytree.right = TreeNode(2)
mytree.left.left = TreeNode(3)
mytree.left.right = TreeNode(4)
mytree.right.left = TreeNode(4)
mytree.right.right = TreeNode(3)
print(path_sum(mytree, 3))
print(path_sum(mytree, 7))
