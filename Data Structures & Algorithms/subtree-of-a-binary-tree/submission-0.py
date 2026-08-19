# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        


    def isSameTree(self, node_A, node_B):
        if node_A is None and node_B is None:
            return True
        elif node_A is not None and node_B is not None:
            return (node_A.val == node_B.val and 
                    self.isSameTree(node_A.left, node_B.left) and
                    self.isSameTree(node_A.right, node_B.right))
        else:
            return False