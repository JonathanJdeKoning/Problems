# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        running = False
        while head:
            v = head.val
            if v in nums:
                if not running:
                    ans += 1
                running = True
            else:
                running = False
            head = head.next
        return ans
