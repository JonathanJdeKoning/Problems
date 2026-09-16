# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        count = 0
        while head:
            head = head.next
            count += 1
        mid = count//2
        prev = dummy
        head = dummy.next
        while mid:
            prev = head
            head = head.next
            mid -= 1

        prev.next = head.next
        return dummy.next
