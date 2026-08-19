# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        valid = False

        if root.left and root.right:
            valid = root.val > root.left.val and root.val < root.right.val

        return (valid and self.isValidBST(root.left) and self.isValidBST(root.right))