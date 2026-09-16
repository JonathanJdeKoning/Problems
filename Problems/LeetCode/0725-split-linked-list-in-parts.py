# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        root = head
        N = 0
        while head:
            N += 1
            head = head.next
        chunks = [N//k]*k
        for i in range(N%k): chunks[i] += 1
        chunks = deque(chunks)
        
        head = root
        ans = []
        nextNode = head
        while chunks:
            l = chunks.popleft()
            if l == 0:
                ans.append(None)
                continue
            head = nextNode
            ans.append(head)
            for _ in range(l-1):
                head = head.next
            nextNode = head.next
            head.next = None
        return ans