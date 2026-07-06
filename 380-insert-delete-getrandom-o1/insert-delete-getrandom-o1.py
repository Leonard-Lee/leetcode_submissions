class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.nums.append(val)
        self.map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        lastVal = self.nums[-1]
        idx = self.map[val]

        # replace
        self.nums[idx] = lastVal
        self.map[lastVal] = idx

        # remove
        self.nums.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()