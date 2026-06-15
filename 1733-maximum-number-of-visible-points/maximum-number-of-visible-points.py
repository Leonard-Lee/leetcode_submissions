class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        if not points:
            return 0

        overlap, degrees = self.transformToDegrees(points, location)
        i = 0
        count = 0
        for j in range(len(degrees)):
            while degrees[i] + angle < degrees[j]:
                i += 1
            count = max(count, j - i + 1)

        return count + overlap

    def transformToDegrees(self, points: List[List[int]], location: List[int]) -> List[int]:
        degrees = []
        overlap = 0

        for px, py in points:
            dx = px - location[0]
            dy = py - location[1]

            if dx == 0 and dy == 0:
                overlap += 1
                continue

            degree = math.degrees(math.atan2(dy, dx))
            if degree < 0:
                degree += 360

            degrees.append(degree)

        degrees.sort()
        return (overlap, degrees + [d + 360 for d in degrees])
        