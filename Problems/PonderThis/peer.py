class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    bfs = deque([(p,q)])

    while bfs:
        nodeP, nodeQ= bfs.popleft()

        if nodeP is None and nodeQ is None:
            continue

        if nodeP is None or nodeQ is None:
            return False
        
        if nodeP.val != nodeQ.val:
            return False
        
        bfs.append((nodeP.left, nodeQ.left))
        bfs.append((nodeP.right, nodeQ.right))
    return True

        

        


def test_isSameTree():
    # Both empty
    assert isSameTree(None, None) == True
    
    # One empty, one not
    assert isSameTree(None, TreeNode(1)) == False
    assert isSameTree(TreeNode(1), None) == False
    
    # Single nodes - same
    assert isSameTree(TreeNode(1), TreeNode(1)) == True
    
    # Single nodes - different
    assert isSameTree(TreeNode(1), TreeNode(2)) == False
    
    # Same structure and values
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTree(tree1, tree2) == True
    
    # Same values, different structure
    tree3 = TreeNode(1, TreeNode(2), None)
    tree4 = TreeNode(1, None, TreeNode(2))
    assert isSameTree(tree3, tree4) == False
    
    # Different values
    tree5 = TreeNode(1, TreeNode(2), TreeNode(1))
    tree6 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert isSameTree(tree5, tree6) == False

test_isSameTree()