# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyboi = head
        while head != None:
            if head.next == None:
                break
            if head.next.val == head.val:
                nextnode = head.next.next
                head.next.next = None
                head.next = nextnode
                continue
            else:
                head = head.next
        return dummyboi
