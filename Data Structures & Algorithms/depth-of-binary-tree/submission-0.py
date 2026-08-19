# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_dep = 0

        def dfs(root):
            nonlocal max_dep

            if root is None:
                return 0

            cur_dep = max(dfs(root.left), dfs(root.right)) + 1
            max_dep = max(cur_dep, max_dep)

            return cur_dep

        dfs(root)
        return max_dep
            