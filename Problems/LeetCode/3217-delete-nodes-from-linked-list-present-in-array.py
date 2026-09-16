# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        if not head:
            return None
        dummy = head
        prev = head
        head = head.next
        while head:
            if head.val in nums:
                prev.next = head.next
                head = head.next
                continue
            else:
                head = head.next
                prev = prev.next
        if dummy.val in nums:
            dummy = dummy.next
        return dummy