from collections import deque
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

def get_reverse_level_order_tree(root: TreeNode):
     result = []

     if not root:
          return result

     node_stack = deque([root])

     while node_stack:
          stack_size = len(node_stack)
          temp = []

          for i in range(stack_size):
               node = node_stack.popleft()
               temp.append(node.val)

               if node.left:
                    node_stack.append(node.left)

               if node.right:
                   node_stack.append(node.right)

          result.append(temp)

     return result[::-1]


mytree = TreeNode(1)
mytree.left = TreeNode(2)
mytree.right = TreeNode(3)
mytree.left.left = TreeNode(4)
mytree.left.right = TreeNode(5)
mytree.right.right = TreeNode(6)
mytree.left.left.left = TreeNode(7)
mytree.left.left.right = TreeNode(8)


output = get_reverse_level_order_tree(mytree)
print(output)
