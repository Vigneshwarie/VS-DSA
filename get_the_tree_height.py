class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []


def get_tree_height(root: TreeNode):
    if root is None:
        return 0

    height = 0

    for child in root.children:
        childHeight = get_tree_height(child) + 1

        if childHeight > height:
            height = childHeight

    return height


mytree = TreeNode(1)
mytree.children = [TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)]
mytree.children[1].children = [TreeNode(6), TreeNode(7)]
mytree.children[2].children = [TreeNode(8)]
mytree.children[3].children = [TreeNode(9), TreeNode(10)]
mytree.children[1].children[1].children = [TreeNode(11)]
mytree.children[2].children[0].children = [TreeNode(12)]
mytree.children[3].children[0].children = [TreeNode(13)]
mytree.children[1].children[1].children[0].children = [TreeNode(14)]

output = get_tree_height(mytree)
print(output)
