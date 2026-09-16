# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd = 0
        eve = 0
        while head:
            if head.val > head.next.val:
                eve += 1
            else:
                odd += 1
            head = head.next
            head = head.next

        if odd == eve:
            return "Tie"
        if odd > eve:
            return "Odd"
        return "Even"
