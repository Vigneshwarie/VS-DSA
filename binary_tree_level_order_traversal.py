from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []


def get_level_order(root: TreeNode) -> List[List[int]]:
    result = []

    if not root:
        return result

    node_queue = deque([root])

    while node_queue:
        q_size = len(node_queue)
        temp = []

        for _ in range(q_size):
            node = node_queue.popleft()
            temp.append(node.val)

            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)

        result.append(temp)

    return result


mytree = TreeNode(1)
mytree.left = TreeNode(2)
mytree.right = TreeNode(3)
mytree.left.left = TreeNode(4)
mytree.left.right = TreeNode(5)
mytree.right.right = TreeNode(6)

# mytree = [3, 9,20,"","",15,7]
output = get_level_order(mytree)
print(output)
