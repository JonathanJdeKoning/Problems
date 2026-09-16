# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []

        while head:
            vals.append(head.val)
            head = head.next

        print(vals)

        s = " ".join(map(str, vals))
        out = s.split(" 0 ")
        new = []
        for x in out:
            new.append(sum(map(int, x.split(" "))))

        print(new)
        dummy = ListNode()

        root = ListNode(val=new[0])
        dummy.next = root
        for x in new[1:]:
            root.next = ListNode(val=x)
            root = root.next
        return dummy.next