# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swapPair(head):
            if not head: return None
            if not head.next: return head
            toReturn = head.next
            tmpNext = swapPair(head.next.next)
            head.next.next = head
            head.next = tmpNext
            return toReturn

        return swapPair(head)
            
