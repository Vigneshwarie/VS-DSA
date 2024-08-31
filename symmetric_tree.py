# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isMirror(tree_x: TreeNode, tree_y: TreeNode):
    if tree_x is None and tree_y is None:
        return True

    if tree_x is None or tree_y is None:
        return False

    if tree_x.val != tree_y.val:
        return False

    return isMirror(tree_x.left, tree_y.right) and isMirror(tree_x.right, tree_y.left)


def isSymmetric(root: TreeNode):
    if root is None:
        return True
    return isMirror(root.left, root.right)


mytree = TreeNode(1)
mytree.left = TreeNode(2)
mytree.right = TreeNode(2)
mytree.left.left = TreeNode(3)
mytree.left.right = TreeNode(4)
mytree.right.left = TreeNode(4)
mytree.right.right = TreeNode(3)


print(isSymmetric(mytree))
