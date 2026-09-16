# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0])
        curr = root
        stack = [root]

        for num in preorder[1:]:
            new = TreeNode(val=num)
            if num < stack[-1].val:
                curr.left = new
                stack.append(new)
                curr = new
            else:
                while num > stack[-1].val:
                    popped = stack.pop()
                    if not stack: break
                popped.right = new
                stack.append(new)
                curr = new
        return root 