# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(tree_x: TreeNode, tree_y: TreeNode):
    if tree_x is None and tree_y is None:
        return True

    if tree_x is None or tree_y is None:
        return False

    if tree_x.val != tree_y.val:
        return False

    return isSameTree(tree_x.left, tree_y.left) and isSameTree(tree_x.right, tree_y.right)


mytree_x = TreeNode(1)
mytree_x.left = TreeNode(2)
mytree_x.right = TreeNode(3)
mytree_x.left.left = TreeNode(4)
mytree_x.left.right = TreeNode(5)
mytree_x.right.right = TreeNode(6)
mytree_x.left.left.left = TreeNode(7)
mytree_x.left.left.right = TreeNode(8)


mytree_y = TreeNode(1)
mytree_y.left = TreeNode(2)
mytree_y.right = TreeNode(3)
mytree_y.left.left = TreeNode(4)
mytree_y.left.right = TreeNode(5)
mytree_y.right.right = TreeNode(6)
mytree_y.left.left.left = TreeNode(7)
mytree_y.left.left.right = TreeNode(9)

print(isSameTree(mytree_x, mytree_y))
