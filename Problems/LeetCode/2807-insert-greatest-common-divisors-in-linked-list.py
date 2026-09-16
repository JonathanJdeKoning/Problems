# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        while head.next:
            x = head.val
            y = head.next.val
            g = gcd(x,y)
            ins = ListNode(val=g, next = head.next)
            head.next = ins
            head = head.next.next
        return dummy.next