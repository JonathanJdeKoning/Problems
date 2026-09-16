class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
            
        if root.val > key:
            root.left = self.deleteNode( root.left, key )
        elif root.val < key:
            root.right = self.deleteNode( root.right, key )

        else:
            if (not root.left) or (not root.right):
                root = root.left if root.left else root.right
            else:
                cur = root.left

                while cur.right:
                    cur = cur.right

                root.val = cur.val
                root.left = self.deleteNode( root.left, cur.val )
                    
        return root