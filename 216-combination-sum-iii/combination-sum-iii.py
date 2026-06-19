class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(idx: int, startNum: int, total: int) -> None:
            if total > target:
                return

            if idx == k:
                if total == target:
                    res.append(cur.copy())
                return

            for i in range(startNum, 10):
                cur.append(i)
                dfs(idx + 1, i + 1, total + i)
                cur.pop()

        dfs(0, 1, 0)
        return res

            
        