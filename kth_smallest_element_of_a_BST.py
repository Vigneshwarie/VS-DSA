class BinarySearchTree:
     def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

def gettheKthSmallestElement(root: BinarySearchTree, k):
     def inordertraversal(node):
          if node is None:
               return None

          nonlocal k

          left = inordertraversal(node.left)
          if left is not None:
               return left

          k = k - 1
          if k == 0:
               return node.val

          return inordertraversal(node.right)
     return inordertraversal(root)


root = BinarySearchTree(5)
root.left = BinarySearchTree(3)
root.right = BinarySearchTree(7)
root.left.left = BinarySearchTree(2)
root.left.right = BinarySearchTree(4)
root.right.left = BinarySearchTree(6)
root.right.right = BinarySearchTree(8)

k = 6
print(gettheKthSmallestElement(root, k))
