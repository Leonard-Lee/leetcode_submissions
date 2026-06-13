class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        overlap_count, degrees = self.pointsToDegrees(points, location)
        i = 0
        count = 0
        maxCount = 0
        for j in range(len(degrees)):
            while degrees[j] > degrees[i] + angle:
                i += 1
            maxCount = max(maxCount, j - i + 1)
        return maxCount + overlap_count

    def pointsToDegrees(self, points: List[List[int]], location: List[int]) -> (int, List[List[int]]):
        n = len(points)
        angles = []
        overlap_count = 0
        for x, y in points:
            dx = x - location[0]
            dy = y - location[1]
            if dx == 0 and dy == 0:
                overlap_count += 1
            else:
                degree = math.degrees(math.atan2(dy, dx))

                if degree < 0:
                    degree += 360

                angles.append(degree)

        angles.sort()
        angles = angles + [d + 360 for d in angles]
        return (overlap_count, angles)
