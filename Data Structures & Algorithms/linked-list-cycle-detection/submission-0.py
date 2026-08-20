# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        res = False
        c1 = head
        c2 = head

        while c1 and c2:
            c1 = c1.next
            c2 = c2.next
            if c2:
                c2 = c2.next

            if c1 == c2:
                return True

        return False 

