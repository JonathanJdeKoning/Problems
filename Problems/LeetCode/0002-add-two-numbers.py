class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        
        head = ListNode(val=None, next=None)
        prev = head
        deathNode = ListNode(val=0, next=None)
        while True:
            ans = l1.val + l2.val + remainder
            rem, base = divmod(ans, 10)
            remainder = rem
            newNode = ListNode(val=base, next=None)

            prev.next = newNode

            if l1.next:
                l1 = l1.next
            else: l1 = deathNode
            if l2.next: 
                l2 = l2.next
            else: l2 = deathNode
            
            prev = newNode

            if l1 == deathNode and l2 == deathNode: break

        
        if remainder:
            prev.next = ListNode(val=1, next=None)

        return head.next
