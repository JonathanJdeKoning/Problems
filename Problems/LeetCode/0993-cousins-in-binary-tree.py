# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([(root, 0)])
        while q:
            level = []
            for _ in range(len(q)):
                mytup = q.popleft()
                level.append(mytup)
                currnode = mytup[0]

                if currnode.left:
                    q.append((currnode.left,currnode))
                if currnode.right:
                    q.append((currnode.right, currnode))
            levelvals = [x[0].val for x in level]
            if x in levelvals and y not in levelvals: 
                print("x in y not")
                return False
            if y in levelvals and x not in levelvals: 
                print("y in x not")
                return False

            if x in levelvals:
                xpar = None
                ypar = None
                for node in level:
                    if node[0].val == x:
                        xpar = node[1]
                    if node[0].val == y:
                        ypar = node[1]
                return xpar != ypar



                