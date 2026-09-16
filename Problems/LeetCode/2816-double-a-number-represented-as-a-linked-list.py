# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
sys.set_int_max_str_digits(1000000)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(str(head.val))
            head = head.next
        new = list([int (x) for x in str(int("".join(arr))*2)])


        start = ListNode(val=new[0])
        dummy = ListNode(next=start)
        for c in new[1:]:
            y = ListNode(val=c)
            start.next = y
            start = y
        return dummy.next
