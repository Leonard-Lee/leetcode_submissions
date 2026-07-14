class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        count = 0
        while l < r:
            if height[l] <= height[r]:
                if lmax > height[l]:
                    count += lmax - height[l]
                else:
                    lmax = height[l]

                l += 1
            else:
                if rmax > height[r]:
                    count += rmax - height[r]
                else:
                    rmax = height[r]

                r -= 1

        return count

        