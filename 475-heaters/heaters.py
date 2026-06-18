class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses or not heaters:
            return 0

        heaters.sort()
        maxRadius = 0
        for house in houses:
            idx = bisect.bisect_left(heaters, house)
            left_radius = house - heaters[idx - 1] if idx > 0 else float("inf")
            right_radius = heaters[idx] - house if idx < len(heaters) else float("inf")
            radius = min(left_radius, right_radius)
            maxRadius = max(maxRadius, radius)
        
        return maxRadius

    def binarySearch(self, heaters, target) -> int:
        l, r = 0, len(heaters)
        while l < r:
            mid = (l + r) // 2

            if heaters[mid] >= target:
                r = mid
            else:
                l = mid + 1
        return l
        