class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # tage each island 
        # hash map mapping tag number to area 
        # go through all the 0s and flip them to connect the largest area

        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visitSet = set()

        def dfs(r, c, tag) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0

            grid[r][c] = tag
            area = 1
            area += dfs(r + 1, c, tag)
            area += dfs(r - 1, c, tag)
            area += dfs(r, c + 1, tag)
            area += dfs(r, c - 1, tag)
            return area

        mapping = {}
        tag = 2
        maxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c, tag)
                    mapping[tag] = area
                    maxArea = max(maxArea, area)
                    tag += 1

        # print(maxArea)
        def helper(r, c):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            area = 1
            visitTags = set()
            visitTags.add(0)

            for dr, dc in directions:
                newr = r + dr
                newc = c + dc
                if newr in range(rows) and newc in range(cols) and grid[newr][newc] not in visitTags:
                    tag = grid[newr][newc]
                    area += mapping[tag]
                    visitTags.add(tag)
            print(area)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    area = helper(r, c)
                    print(area)
                    maxArea = max(maxArea, area)
        
        return maxArea


            
        