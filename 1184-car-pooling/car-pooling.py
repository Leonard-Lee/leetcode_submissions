class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        
        times = []
        for cap, start, end in trips:
            times.append((start, cap))
            times.append((end, -cap))

        times.sort()
        count = 0

        for time, change in times:
            count += change
            if capacity < count:
                return False

        return True

        