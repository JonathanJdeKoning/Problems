# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        seen.add(headA)
        while headA.next:
            headA = headA.next
            seen.add(headA)
        while headB.next:
            if headB in seen:
                return headB
            headB = headB.next
        
        if headA == headB: return headA
        return None