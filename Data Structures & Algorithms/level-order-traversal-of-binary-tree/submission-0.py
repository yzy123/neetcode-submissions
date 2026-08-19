# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])

        while queue:
            qlen = len(queue)
            cur_level_res = []
            for _ in range(qlen):
                node = queue.popleft()
                if node is not None:
                    cur_level_res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if (len(cur_level_res) != 0):
                res.append(cur_level_res)

        return res

