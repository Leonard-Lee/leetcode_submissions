class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        newCosts = [0] + costs

        # n is the stair and the output is the minimum cost
        # memo = {}
        # def dfs(n) -> int:
        #     if n in memo:
        #         return memo[n]
        #     if n <= 0:
        #         memo[n] = 0
        #         return 0

        #     memo[n] = newCosts[n] + min(9 + dfs(n - 3), 4 + dfs(n - 2), 1 + dfs(n - 1))
        #     return memo[n]

        # return dfs(n)
        memo = [0] * (n + 1)
        memo[0] = 0
        for i in range(1, n + 1):
            jump1 = 1 + memo[i - 1] if i >= 1 else float("inf")
            jump2 = 4 + memo[i - 2] if i >= 2 else float("inf")
            jump3 = 9 + memo[i - 3] if i >= 3 else float("inf")
            memo[i] = newCosts[i] + min(jump1, jump2, jump3)

        return memo[n]

        