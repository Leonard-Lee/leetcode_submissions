class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        overlap, degrees = self.transformToDegrees(points, location)
        count = 0
        print(degrees)
        i = 0
        for j in range(len(degrees)):
            while degrees[i] + angle < degrees[j]:
                i += 1
            
            count = max(count, j - i + 1)

        return count + overlap
        


    # transform all the points based on the location to degrees
    def transformToDegrees(self, points: List[List[int]], location: List[int]) -> Tuple:
        degrees = []
        overlap = 0
        for px, py in points:
            dy = py - location[1]
            dx = px - location[0]
            if dy == 0 and dx == 0:
                overlap += 1
                continue 

            degree = math.degrees(math.atan2(dy, dx))
            if degree < 0:
                degree += 360
            degrees.append(degree)

        degrees.sort()
        return (overlap, degrees + [d + 360 for d in degrees])





        