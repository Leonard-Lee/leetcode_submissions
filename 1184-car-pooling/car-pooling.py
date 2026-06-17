class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        if not trips:
            return True
        
        times = []
        for cap, start, end in trips:
            times.append((start, cap))
            times.append((end, -cap))

        times.sort()
        # key: use a seperate count because we need end to be negative for the tie case. So capacity will be released before taken again
        # trips = [[2,1,5],[3,5,7]]
        # cap = 3
        count = 0

        for time, change in times:
            count += change
            if capacity < count:
                return False

        return True

        