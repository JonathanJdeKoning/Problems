"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        root = head
        while head:
            new = Node(head.val)
            new.next = head.next
            head.next = new
            head = head.next.next
        head = root
        child = None
        while head:
            child = head.next
            
            if head.random is not None:
                head.next.random = head.random.next
            head = head.next.next

            if child is not None and head is not None:
                child.next = head.next
        return root.next
