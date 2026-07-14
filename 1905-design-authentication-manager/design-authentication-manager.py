class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.map = OrderedDict()
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.evict(currentTime)
        self.map[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        self.evict(currentTime)
        if tokenId in self.map:
            self.map[tokenId] = currentTime + self.ttl
            self.map.move_to_end(tokenId)
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.evict(currentTime)
        return len(self.map)
        
    def evict(self, currentTime: int) -> None:
        while self.map and next(iter(self.map.values())) <= currentTime:
            self.map.popitem(last=False)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)