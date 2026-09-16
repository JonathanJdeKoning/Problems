# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if (target - 0.5).is_integer():
            target = floor(target)
        else:
            target = round(target)

        mnDist = inf
        best = None
        while root:
            v = root.val
            dist = abs(v - target)
            if v == target: return v
            if dist < mnDist:
                mnDist = dist
                best = v
            elif dist == mnDist: best = min(best, v)

            if v > target:
                root = root.left
            elif v < target:
                root = root.right
            else:
                print("SOMETHING HAS GONE HORRIBLY WRONG")
        return best
            

             
