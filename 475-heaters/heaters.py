class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        if not houses or not heaters:
            return 0

        houses.sort()
        heaters.sort()

        idx = 0 # idx for heaters
        maxRadius = 0
        for house in houses:
            while idx < len(heaters) - 1 and abs(house - heaters[idx]) >= abs(house - heaters[idx + 1]):
                idx += 1

            maxRadius = max(maxRadius, abs(house - heaters[idx]))
        return maxRadius

        