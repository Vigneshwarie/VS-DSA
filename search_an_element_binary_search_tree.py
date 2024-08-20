class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def element_in_a_binary_search_tree(root: BinaryTree, key):
    if root is None:
        return 0

    if root.val == key:
        return 1

    if root.val > key:
        return element_in_a_binary_search_tree(root.left, key)
    else:
        return element_in_a_binary_search_tree(root.right, key)


mytree = BinaryTree(4)
mytree.left = BinaryTree(2)
mytree.right = BinaryTree(6)
mytree.left.left = BinaryTree(1)
mytree.left.right = BinaryTree(3)
mytree.right.left = BinaryTree(5)
mytree.right.right = BinaryTree(7)


# output = element_in_a_binary_search_tree(mytree, 3)
print(element_in_a_binary_search_tree(mytree, 17))
# print(output)
