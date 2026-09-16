class DLL:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def popTail(self):
        if not self.tail: return
        if not self.tail.next:
            self.tail = None
            return

        self.tail.next.prev = None
        self.tail = self.tail.next

    def popHead(self):
        if not self.head: return
        if not self.head.prev:
            self.head = None
            return
        self.head.prev.next = None
        self.head = self.head.prev
    
    def popNode(self, node):
        if not node: return
        if self.head == node and self.tail==node:
            self.head = None
            self.tail = None
            return

        if self.head == node:
            self.popHead()
            return
        
        if self.tail == node:
            self.popTail()
            return
        
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def pushHead(self, node):
        node.next = None
        if not node: return
        if not self.tail:
            self.tail = node

        if not self.head:
            self.head = node
        else:
            self.head.next = node
            node.prev = self.head
            self.head = node
    
class Node:
    def __init__(self, key=None ,val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DLL()
        self.key2node = {}


    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        self.renew(key)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.renew(key)
            return
        
        if len(self.key2node) == self.capacity:
            lru = self.dll.tail
            self.evict(lru.key)
        
        new = Node(key, value)
        self.key2node[key] = new
        self.dll.pushHead(new)


    def evict(self, key):
        node = self.key2node[key]
        self.dll.popNode(node)
        del self.key2node[key]
        
    def renew(self, key):
        node = self.key2node[key]
        self.dll.popNode(node)
        self.dll.pushHead(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)