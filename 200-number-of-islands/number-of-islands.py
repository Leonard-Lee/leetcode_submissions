class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visitSet = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visitSet or grid[r][c] == "0":
                return

            visitSet.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visitSet and grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count