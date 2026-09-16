# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        twins = []
        while head:
            twins.append(head.val)
            head = head.next

        return max([twins[i] + twins[~i] for i in range(len(twins)//2)])