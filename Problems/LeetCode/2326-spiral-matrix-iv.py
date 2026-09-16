# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1]*n for _ in range(m)]
        cy, cx = 0,0
        dy, dx = 0, 1

        while head:
            ans[cy][cx] = head.val
            ny, nx = cy+dy, cx+dx
            if (ny not in range(m)) or (nx not in range(n)) or ans[ny][nx] != -1:
                dy, dx = dx, -dy
                ny, nx = cy+dy, cx+dx
            cy, cx = ny, nx


            head = head.next
        return ans