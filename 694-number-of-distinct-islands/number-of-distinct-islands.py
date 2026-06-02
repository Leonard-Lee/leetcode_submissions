class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        resSet = set()
        visitSet = set()

        def dfs(r, c, originr, originc) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return

            if (r - originr, c - originc) in visitSet:
                return

            grid[r][c] = 0
            visitSet.add((r - originr, c - originc))
            dfs(r + 1, c, originr, originc)
            dfs(r - 1, c, originr, originc)
            dfs(r, c + 1, originr, originc)
            dfs(r, c - 1, originr, originc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    visitSet = set()
                    dfs(r, c, r, c)
                    resSet.add(frozenset(visitSet))
                
        return len(resSet)

            
        