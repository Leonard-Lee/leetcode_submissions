class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        dp = {}

        # input: cur idx
        # output: max profit
        def dfs(idx: int) -> int:
            if idx in dp:
                return dp[idx]

            if idx >= len(intervals):
                dp[idx] = 0
                return 0

            # not pick
            skip = dfs(idx + 1)

            # pick the current interval
            newIdx = bisect.bisect_left(intervals, (intervals[idx][1], -1, -1))
            include = intervals[idx][2] + dfs(newIdx)

            dp[idx] = max(skip, include)
            return dp[idx]

        return dfs(0)




        