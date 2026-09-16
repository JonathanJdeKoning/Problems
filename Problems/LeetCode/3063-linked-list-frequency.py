# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        mp = {}
        while head:
            v = head.val
            if v not in mp:
                newNode = ListNode(val=1, next=prev)
                mp[v] = newNode
                prev = newNode
            else:
                mp[v].val += 1

            head = head.next
        return prev