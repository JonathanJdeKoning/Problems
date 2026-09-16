# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        bad = set()
        seen = set()
        dummy = ListNode(next = head)
        while head:
            if head.val in seen:
                bad.add(head.val)
            else:
                seen.add(head.val)
            head = head.next

        head = dummy.next
        prev = dummy
        while head:
            if head.val in bad:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
