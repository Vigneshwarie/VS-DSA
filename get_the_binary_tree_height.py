class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_binary_tree_height(root: BinaryTree):
    if root is None:
        return 0
    else:
        height = 1

    leftHeight = get_binary_tree_height(root.left)
    rightHeight = get_binary_tree_height(root.right)

    maxHeight = max(leftHeight, rightHeight) + height

    return maxHeight


mytree = BinaryTree(1)
mytree.left = BinaryTree(2)
mytree.right = BinaryTree(3)
mytree.left.left = BinaryTree(4)
mytree.left.right = BinaryTree(5)
mytree.right.right = BinaryTree(6)
mytree.left.left.left = BinaryTree(7)
mytree.left.left.right = BinaryTree(8)


output = get_binary_tree_height(mytree)
print(output)
