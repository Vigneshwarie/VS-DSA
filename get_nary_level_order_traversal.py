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


def get_nary_level_order(root: Node) -> List[List[int]]:
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

            for child in node.children:
                node_queue.append(child)

        result.append(temp)

    return result


# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
mytree = Node(1)
mytree.children = [Node(2), Node(3), Node(4), Node(5)]
mytree.children[1].children = [Node(6), Node(7)]
mytree.children[2].children = [Node(8)]
mytree.children[3].children = [Node(9), Node(10)]
mytree.children[1].children[1].children = [Node(11)]
mytree.children[2].children[0].children = [Node(12)]
mytree.children[3].children[0].children = [Node(13)]
mytree.children[1].children[1].children[0].children = [Node(14)]




# mytree = [3, 9,20,"","",15,7]
output = get_nary_level_order(mytree)
print(output)
