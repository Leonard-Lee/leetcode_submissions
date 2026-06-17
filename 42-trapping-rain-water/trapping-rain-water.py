class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        l, r = 0, len(heights) - 1
        lmax, rmax = 0, 0
        count = 0

        while l < r:
            if heights[l] < heights[r]:
                if heights[l] < lmax:
                    count += lmax - heights[l]
                else:
                    lmax = heights[l]
                l += 1
            else:
                if heights[r] < rmax:
                    count += rmax - heights[r]
                else:
                    rmax = heights[r]
                r -= 1

        return count
        