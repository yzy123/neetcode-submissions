# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        
        res = 0
        k_small = 0
        def samllest(root):
            nonlocal res, k_small
            if not root:
                return

            samllest(root.left)
            k_small += 1
            if k_small == k:
                res = root.val
            samllest(root.right)
            return

        samllest(root)
        return res
        

            
            