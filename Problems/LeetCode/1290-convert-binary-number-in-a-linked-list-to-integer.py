# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
            num = []

            while head:
                num.append(str(head.val))
                head = head.next
            smushed = "".join(num)
            return int(smushed, 2) 