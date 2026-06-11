class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        # sort the points 
        points.sort()
        res = [0] * len(queries)

        # use bounding box
        for i in range(len(queries)):
            cx, cy, r = queries[i]
            left = cx - r
            right = cx + r

            # print("left: " + str(left) + " right: " + str(right))
            leftIdx = self.binarySearch(points, left)
            rightIdx = self.binarySearch(points, right + 1)

            for j in range(leftIdx, rightIdx):
                px, py = points[j]
                if (px - cx) ** 2 + (py - cy) ** 2 <= r ** 2:
                    res[i] += 1
        return res

    def binarySearch(self, points: List[List[int]], x: int) -> int:
        l, r = 0, len(points)
        while l < r:
            mid = (l + r) // 2
            if points[mid][0] >= x:
                r = mid
            else:
                l = mid + 1
        return l

        