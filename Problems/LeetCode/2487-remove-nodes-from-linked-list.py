# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr= []
        while head:
            arr.append(head.val)
            head = head.next

        arr = arr[::-1]
        mx = arr[0]
        new = [arr[0]]
        for x in arr[1:]:
            if x >= mx:
                new.append(x)
            mx = max(mx, x)
        if not new: return None
        start = ListNode(val=new[0])
        for x in new[1:]:
            y = ListNode(val=x, next=start)
            start = y
        return start
