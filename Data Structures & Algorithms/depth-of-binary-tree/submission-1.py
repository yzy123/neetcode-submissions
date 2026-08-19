# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        stack   = [[root, 1]]
        max_dep = 0

        while len(stack) != 0:
            node, cur_dep = stack.pop()
            if node:
                max_dep = max(cur_dep, max_dep)

                stack.append([node.left, cur_dep + 1])
                stack.append([node.right, cur_dep + 1])

        return max_dep