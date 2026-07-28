class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        n = len(costs)
        prepre = 0
        pre = 0
        for i in range(2, n + 1):
            cur = min(prepre + costs[i - 2], pre + costs[i - 1])
            prepre = pre
            pre = cur

        return pre
        