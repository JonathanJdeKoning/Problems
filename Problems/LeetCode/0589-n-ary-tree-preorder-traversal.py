"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        out = []
        def pre(node):
            if not node: return

            out.append(node.val)
            for child in node.children:
                pre(child)
        pre(root)
        return out
                  