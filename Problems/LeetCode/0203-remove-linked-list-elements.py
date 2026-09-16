# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        prev = ListNode(next=head)
        if not head: return None
        foundGood = False
        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
                continue
            else:
                if not foundGood:
                    dummy.next = head
                    foundGood = True

            prev = prev.next
            head = head.next

        return dummy.next
