# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = list1
        for _ in range(a-1):
            list1 = list1.next
        post = list1
        for _ in range((b-a)+2):
            list1 = list1.next
        post2 = list1
        post.next = list2
        
        while list2.next:
            list2 = list2.next
        list2.next = post2
        return dummy.next