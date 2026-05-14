class Node:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # map a key to a node
        self.map = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
            
        node = self.map[key]
        self.remove(node)
        self.insertToTail(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.remove(node)

        newNode = Node(key, value)
        self.map[key] = newNode
        self.insertToTail(newNode)

    def remove(self, node: Node) -> None:
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre

    def insertToTail(self, node: Node) -> None:
        preTail = self.tail.pre
        preTail.next = node
        node.pre = preTail

        node.next = self.tail
        self.tail.pre = node

        if len(self.map) > self.cap:
            deletedNode = self.head.next
            self.remove(deletedNode)
            del self.map[deletedNode.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)