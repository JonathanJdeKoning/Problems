# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head: return None
        if not head.next: return head
        dummy = ListNode(next = head)
        eveDummy = head.next

        oddHead = head
        eveHead = head.next

        while oddHead.next and eveHead.next:
            oddHead.next = eveHead.next
            eveHead.next = eveHead.next.next

            oddHead = oddHead.next
            eveHead = eveHead.next

        oddHead.next = eveDummy
        
        return dummy.next