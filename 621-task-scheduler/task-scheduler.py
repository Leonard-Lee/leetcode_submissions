class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0

        countMap = {}
        for task in tasks:
            countMap[task] = countMap.get(task, 0) + 1

        maxHeap = [ -count for count in countMap.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0
        while maxHeap or q:
            if maxHeap:
                count = heapq.heappop(maxHeap) + 1
                if count != 0:
                    q.append((count, time + n))
            else:
                time = q[0][1]

            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])

            time += 1
        return time

        