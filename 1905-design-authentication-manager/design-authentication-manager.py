class ListNode:
    def __init__(self, key="", val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        # map a token id to a double linked list node
        self.map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.pre = self.head

    def generate(self, tokenId: str, currentTime: int) -> None:
        if len(self.map) > 0:
            self.countUnexpiredTokens(currentTime)

        node = ListNode(tokenId, currentTime + self.ttl)
        self.map[tokenId] = node
        self.insertToTail(node)

    def renew(self, tokenId: str, currentTime: int) -> None:
        if len(self.map) > 0:
            self.countUnexpiredTokens(currentTime)
        
        if tokenId not in self.map:
            return

        node = self.map[tokenId]
        self.remove(node)
        newNode = ListNode(tokenId, currentTime + self.ttl)
        self.map[tokenId] = newNode
        self.insertToTail(newNode)

    # amortized O(1)
    def countUnexpiredTokens(self, currentTime: int) -> int:
        cur = self.head.next
        while cur.key != "" and currentTime >= cur.val:
            nxt = cur.next
            self.remove(cur)
            del self.map[cur.key]
            cur = nxt

        return len(self.map)
        
    def remove(self, node: ListNode) -> None:
        pre = node.pre
        nxt = node.next
        pre.next = nxt
        nxt.pre = pre

        node.pre = None
        node.next = None

    def insertToTail(self, node: ListNode) -> None:
        preTail = self.tail.pre
        preTail.next = node
        node.pre = preTail

        node.next = self.tail
        self.tail.pre = node

        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)