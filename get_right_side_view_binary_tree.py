from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def display_right_side_view(root: TreeNode):
    result = []

    if not root:
        return result

    node_queue = deque([root])
    while node_queue:
        queue_size = len(node_queue)

        for i in range(queue_size):
            node = node_queue.popleft()

            if i == queue_size - 1:
                result.append(node.val)

            if node.left:
                node_queue.append(node.left)
            if node.right:
                node_queue.append(node.right)

    return result


mytree = TreeNode(1)
mytree.left = TreeNode(2)
mytree.right = TreeNode(3)
mytree.left.left = TreeNode(4)
mytree.left.right = TreeNode(5)
mytree.right.right = TreeNode(6)
mytree.left.left.left = TreeNode(7)
mytree.left.left.right = TreeNode(8)


output = display_right_side_view(mytree)
print(output)
