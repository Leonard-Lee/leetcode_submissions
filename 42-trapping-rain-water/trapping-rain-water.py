class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        # from left to right 
        n = len(heights)
        pre = 0
        lefts = [0] * n
        for i in range(n):
            lefts[i] = pre
            pre = max(pre, heights[i])

        pre = 0
        rights = [0] * n
        for i in range(n - 1, -1, -1):
            rights[i] = pre
            pre = max(pre, heights[i])

        count = 0
        for i in range(n):
            barHeight = min(lefts[i], rights[i])
            if barHeight > heights[i]:
                count += barHeight - heights[i]
        
        return count
        