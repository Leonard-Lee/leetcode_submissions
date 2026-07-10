class Solution:
    # visit each island, tag them, and calculate their area
    # map tag nums to area
    # iterate all 0 cells, find the max area
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        # return total area
        def dfs(r: int, c: int, tag: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0

            grid[r][c] = tag
            area = 1
            area += dfs(r + 1, c, tag) + dfs(r - 1, c, tag) + dfs(r, c + 1, tag) + dfs(r, c - 1, tag)
        
            return area

        mapping = {}
        tag = 2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c, tag)
                    print(area)
                    mapping[tag] = area
                    tag += 1

        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visitSet = set()
                    area = 1
                    for dr, dc in dirs:
                        newr = r + dr
                        newc = c + dc
                        if newr in range(rows) and newc in range(cols) and grid[newr][newc] not in visitSet and grid[newr][newc] != 0:
                            tag = grid[newr][newc]
                            area += mapping[tag]
                            visitSet.add(tag)
                        maxArea = max(maxArea, area)

        return maxArea if maxArea != 0 else rows * cols


