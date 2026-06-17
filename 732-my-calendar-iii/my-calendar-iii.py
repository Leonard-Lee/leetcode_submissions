class MyCalendarThree:

    def __init__(self):
        self.timelines = SortedDict()
        

    def book(self, startTime: int, endTime: int) -> int:
        self.timelines[startTime] = self.timelines.get(startTime, 0) + 1
        self.timelines[endTime] = self.timelines.get(endTime, 0) - 1

        maxCount = 0
        count = 0
        for key, val in self.timelines.items():
            count += val
            maxCount = max(maxCount, count)

        return maxCount
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)