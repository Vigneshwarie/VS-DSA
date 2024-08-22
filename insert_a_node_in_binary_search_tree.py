class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_in_a_binary_search_tree(root: BinaryTree, k):

    if root is None:
        return BinaryTree(k)

    if k < root.val:
        root.left = insert_in_a_binary_search_tree(root.left, k)
    elif k > root.val:
        root.right = insert_in_a_binary_search_tree(root.right, k)

    return root


mytree = BinaryTree(4)
mytree.left = BinaryTree(2)
mytree.right = BinaryTree(6)
mytree.left.left = BinaryTree(1)
mytree.left.right = BinaryTree(3)
mytree.right.left = BinaryTree(5)
mytree.right.right = BinaryTree(7)

# output = element_in_a_binary_search_tree(mytree, 3)
print(insert_in_a_binary_search_tree(mytree, 17))
# print(output)
