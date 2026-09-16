# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def condition(n):
            head = root
            trav = []
            for _ in range(depth):
                trav.append(n & 1)
                n >>= 1
            trav = trav[::-1]
            print(trav, end = ": ")

            for t in trav[:-1]:
                if t == 0:
                    head = head.left
                else:
                    head = head.right
            if trav[-1] == 0:
                print(head.left is None)
                return head.left is None
            else:
                print(head.right is None)
                return head.right is None


        def subtreeDepth(root):
            if root.left:
                return subtreeDepth(root.left) + 1
            return 0



        depth = subtreeDepth(root)
        if depth == 0: return 1
        print(depth)
        head = root
        d=0
        while head.right:
            head = head.right
            d += 1
        if d == depth:
            return 2**(depth+1) - 1
        low = 0
        high = 2**depth-1 

        while low < high:
            mid = (low + high) // 2
            print(f"Mid: {mid}")
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        print(f"Low: {low}")
        return low + (2**depth-1)
        