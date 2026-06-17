class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        maxCount = 0
        if not intervals:
            return maxCount

        times = []
        for start, end in intervals:
            times.append((start, 1))
            times.append((end, -1))

        times.sort()
        count = 0
        for time, change in times:
            count += change
            maxCount = max(maxCount, count)

        return maxCount

        