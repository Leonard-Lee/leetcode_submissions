class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))

        n = len(startTime)
        dp = {}
        dp[n] = 0
        # regarding the idx, return the max profit
        def dfs(idx: int) -> int:
            if idx in dp:
                return dp[idx]

            # skip the current profit
            res = dfs(idx + 1)
            # take the current profit and find the next start index
            newIdx = bisect.bisect_left(intervals, intervals[idx][1], key=lambda x: x[0])
            dp[idx] = max(res, intervals[idx][2] + dfs(newIdx))
            return dp[idx]

        return dfs(0)

        