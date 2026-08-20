# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = pre = None

        while second:
            temp        = second.next
            second.next = pre
            pre         = second
            second      = temp

        n1, n2 = head, pre

        while n2:
            tmp1, tmp2 = n1.next, n2.next
            n1.next = n2
            n2.next = tmp1
            n1, n2 = tmp1, tmp2