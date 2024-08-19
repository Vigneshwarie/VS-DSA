class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_inorder_traversal(root: BinaryTree):
    if root is None:
        return

    if root.left:
        print_inorder_traversal(root.left)

    print(root.val, end=" ")

    if root.right:
        print_inorder_traversal(root.right)


mytree = BinaryTree(1)
mytree.left = BinaryTree(2)
mytree.right = BinaryTree(3)
mytree.left.left = BinaryTree(4)
mytree.left.right = BinaryTree(5)
mytree.right.right = BinaryTree(6)
mytree.left.left.left = BinaryTree(7)
mytree.left.left.right = BinaryTree(8)

print_inorder_traversal(mytree)
