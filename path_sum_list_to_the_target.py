# Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

# A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum_list(root: TreeNode, targetSum: int):
    def helper(node: TreeNode, currentSum: int, path: list, result: list):
        if node is None:
            return result

        currentSum += node.val
        path.append(node.val)

        if node.left is None and node.right is None:
            if currentSum == targetSum:
                result.append(list(path))

        helper(node.left, currentSum, path, result)
        helper(node.right, currentSum, path, result)

        path.pop()

    result = []
    helper(root, 0, [], result)
    return result


mytree = TreeNode(5)
mytree.left = TreeNode(4)
mytree.left.left = TreeNode(11)
mytree.left.left.left = TreeNode(7)
mytree.left.left.right = TreeNode(2)
mytree.right = TreeNode(8)
mytree.right.left = TreeNode(13)
mytree.right.right = TreeNode(4)
mytree.right.right.left = TreeNode(5)
mytree.right.right.right = TreeNode(1)

print(path_sum_list(mytree, 22))
