class Solution:
    def climbStairs(self, n: int) -> int:
        prepre = 1
        pre = 1

        for i in range(2, n + 1):
            cur = pre + prepre
            prepre = pre
            pre = cur

        return pre
        