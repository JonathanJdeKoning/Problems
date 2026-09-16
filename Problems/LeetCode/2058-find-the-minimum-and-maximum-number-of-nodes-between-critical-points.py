# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = None
        curr = head
        aftr = head.next
        crits = []
        node = 1
        while True:
            node += 1
            prev,curr,aftr = curr, aftr, aftr.next
            if aftr is None: break

            a,b,c = prev.val, curr.val, aftr.val


            

            if (b >a and b > c) or (b <a and b < c):
                crits.append(node)

        if len(crits) < 2: return [-1,-1]
        mn = inf
        for a,b in pairwise(crits):
            mn = min(mn, b-a)
        mx = crits[-1] - crits[0]
        return[mn,mx]

