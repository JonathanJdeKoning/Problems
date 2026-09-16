# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head)
            head = head.next
        arr = sorted(arr, key=lambda x:x.val)
        arr.append(None)
        for i, c in enumerate(arr[:-1]):
            c.next = arr[i+1]
        return arr[0]