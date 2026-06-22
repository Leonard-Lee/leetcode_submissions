class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(idx: int, startNum: int, sum: int) -> None:
            if idx == k:
                if sum == n:
                    res.append(cur.copy())
                return

            for i in range(startNum, 10):
                cur.append(i)
                dfs(idx + 1, i + 1, sum + i)
                cur.pop()

        dfs(0, 1, 0)
        return res
            

        