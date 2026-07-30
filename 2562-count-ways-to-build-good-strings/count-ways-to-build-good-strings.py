class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7

        # "00", "11", "000", "110", "011"
        memo = {}
        def dfs(idx) -> int:
            if idx in memo:
                return memo[idx]

            if idx > high:
                memo[idx] = 0
                return 0

            count = 0
            if idx >= low:
                count = 1

            memo[idx] = (count + dfs(idx + zero) + dfs(idx + one)) % MOD
            return memo[idx]
        
        return dfs(0)


        