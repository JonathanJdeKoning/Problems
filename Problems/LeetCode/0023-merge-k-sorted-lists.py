# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)
        h = [(nodeList) for nodeList in lists if nodeList]
        heapify(h)
        dummy = ListNode()
        prev = dummy

        while h:
            n = heappop(h)

            prev.next = n
            prev = prev.next
            if n.next:
                heappush(h, (n.next))
        return dummy.next
