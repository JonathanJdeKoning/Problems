# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.good = set()
        s = [(root, 0)]
        while s:
            curr, val = s.pop()

            self.good.add(val)
            if curr.left:
                s.append((curr.left, 2*val+1))
            if curr.right:
                s.append((curr.right, 2*val+2))

    def find(self, target: int) -> bool:
        return target in self.good
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)