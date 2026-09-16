# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        n = 0
        while head:
            head = head.next
            n += 1
        
        if n <= 1: return dummy.next

        check = set([k-1, n-k])
        found = []
        x = 0
        head = dummy.next
        while head:
            if x in check:
                found.append(head)
            head = head.next
            x += 1 
        if len(found) == 1: return dummy.next
        found[0].val, found[1].val = found[1].val, found[0].val
        return dummy.next