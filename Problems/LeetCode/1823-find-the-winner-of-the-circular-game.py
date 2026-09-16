class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        prev = ListNode(val=1)
        start = prev
        for i in range(2,n+1):
            new = ListNode(val=i)
            prev.next = new
            prev = new
        prev.next = start
        curr = start
        for i in range(n-1):
            for _ in range(k-1):
                prev = curr
                curr = curr.next
            prev.next = curr.next
            curr = curr.next
        return curr.val

