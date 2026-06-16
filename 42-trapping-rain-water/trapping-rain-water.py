class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        lmax, rmax = 0, 0
        n = len(heights)
        # two pointers
        l, r = 0, n - 1
        count = 0
        while l < r:
            if heights[l] < heights[r]:
                if heights[l] > lmax:
                    lmax = heights[l]
                else:
                    count += lmax - heights[l]
                l += 1
            else:
                if heights[r] > rmax:
                    rmax = heights[r]
                else:
                    count += rmax - heights[r]
                r -= 1
        return count 