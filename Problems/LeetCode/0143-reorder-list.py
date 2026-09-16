# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(next=head)
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        rev = None
        while mid:
            mid.next, mid, rev = rev, mid.next, mid
        revhead = rev
        print(head.val)
        print(revhead.val)
        while head:
            leftnext = head.next
            rightnext= revhead.next
            head.next = revhead
            revhead.next = leftnext
            revhead = rightnext
            head = leftnext
        return dummy.next
