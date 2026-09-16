# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        while True:
            for _ in range(m-1):
                if not head: return dummy.next
                head = head.next
            jmp = head
            for _ in range(n):
                if not jmp: return dummy.next
                if not jmp.next:
                    break
                jmp = jmp.next
            head.next = jmp.next
            head = jmp.next
        return dummy.next