class ListNode:
    def __init__(self, next, val):
        self.next = next
        self.val = val

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None        

    def get(self, index: int) -> int:
        newNode = self.head
        for _ in range(index):
            if newNode == None:
                return -1
            newNode = newNode.next
        if newNode == None:
            return -1
        return newNode.val

    def addAtHead(self, val: int) -> None:
        newHead = ListNode(self.head, val)
        self.head = newHead
        if self.head.next is None:
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(None, val)
        if self.tail:
            self.tail.next = newNode

        self.tail = newNode
        if self.head is None:
            self.head = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            newHead = ListNode(self.head, val)
            self.head = newHead
            # Added an early return 
            return
            
        curr = self.head
        for _ in range(index - 1):
            if curr == None:
                return
            curr = curr.next
            
        if curr == None:
            return
        
        newNode = ListNode(curr.next, val)
        curr.next = newNode
        
        if curr == self.tail:
            self.tail = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and not self.head: return
        
        if index == 0:
            self.head = self.head.next
            return
        
        
        curr = self.head
        prev = None
        for _ in range(index):
            prev = curr
            curr = curr.next
            if curr is None: return
            
        prev.next = curr.next
        if prev.next is None:
            self.tail = prev
        
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)