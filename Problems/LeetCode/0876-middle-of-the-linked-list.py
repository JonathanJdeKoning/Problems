class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def listLength(root):
            nodeCount = 0
            while root:
                nodeCount += 1
                root = root.next
            return nodeCount

        length = listLength(head)
        mid = length // 2

        for _ in range(mid):
            head = head.next
        return head