# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        parents = {root: None}
        stack = [(root,None)]
        leaves = []
        total = 0
        while stack:
            node = stack.pop()
            curr= node[0]
            parent = node[1]
            parents[curr] = parent

            if curr.left: stack.append((curr.left,curr))
            if curr.right: stack.append((curr.right,curr))

            if not curr.left and not curr.right: leaves.append(curr)
        
    
        for leaf in leaves:
            nums = []
            nums.append(str(leaf.val))
            while parents[leaf] != None:
                leaf = parents[leaf]
                nums.append(str(leaf.val))
            b = "".join(nums[::-1])
            total += int(b,2)
        return total
