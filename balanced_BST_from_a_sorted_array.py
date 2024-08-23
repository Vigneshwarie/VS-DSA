class BinaryTree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.val}, {self.left}, {self.right})"


def build_bst_from_sorted_array(sortedarray):
    def bstHelper(sortedarray, start, end):
        if start > end:
            return None

        mid = start + (end-start) // 2

        root = BinaryTree(sortedarray[mid])

        root.left = bstHelper(sortedarray, start, mid-1)
        root.right = bstHelper(sortedarray, mid+1, end)

        return root

    return bstHelper(sortedarray, 0, len(sortedarray)-1)


sortedarray = [2, 5, 6, 9, 12]
output = build_bst_from_sorted_array(sortedarray)
print(output)
