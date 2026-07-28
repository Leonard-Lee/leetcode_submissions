class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        newCosts = [0] + costs

        # n is the stair and the output is the minimum cost
        memo = {}
        def dfs(n) -> int:
            if n in memo:
                return memo[n]
            if n <= 0:
                memo[n] = 0
                return 0

            memo[n] = newCosts[n] + min(9 + dfs(n - 3), 4 + dfs(n - 2), 1 + dfs(n - 1))
            return memo[n]

        return dfs(n)
        