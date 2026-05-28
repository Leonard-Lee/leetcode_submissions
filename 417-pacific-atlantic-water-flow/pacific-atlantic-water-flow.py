class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        pacSet = set()
        altSet = set()

        def dfs(r, c, visitSet, preHeight) -> None:
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visitSet or heights[r][c] < preHeight:
                return

            visitSet.add((r, c))
            dfs(r + 1, c, visitSet, heights[r][c])
            dfs(r - 1, c, visitSet, heights[r][c])
            dfs(r, c + 1, visitSet, heights[r][c])
            dfs(r, c - 1, visitSet, heights[r][c])

        for c in range(cols):
            dfs(0, c, pacSet, heights[0][c])
            dfs(rows - 1, c, altSet, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pacSet, heights[r][0])
            dfs(r, cols - 1, altSet, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacSet and (r, c) in altSet:
                    res.append([r, c])
        return res
        