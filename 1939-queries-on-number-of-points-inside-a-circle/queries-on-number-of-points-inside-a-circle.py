class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        if not points or not queries:
            return res

        # sort the points by x, and then by y if they tie
        points.sort()
        res = []
        for x, y, r in queries:
            low = self.binarySearch(points, x - r)
            high = self.binarySearch(points, x + r + 1)
            # # print("low: " + str(low))
            # print("high: " + str(high))
            count = 0
            for idx in range(low, high):
                px, py = points[idx]
                if (px - x) ** 2 + (py - y) ** 2 <= r ** 2:
                    count += 1
            res.append(count)

        return res

    def binarySearch(self, points: List[int][int], target: int) -> int:
        l, r = 0, len(points)
        while l < r:
            mid = (l + r) // 2
            if points[mid][0] >= target:
                r = mid
            else:
                l = mid + 1

        return l 
        
        