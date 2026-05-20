class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # map a word to its frequency
        countMap = defaultdict(int)
        for word in words:
            countMap[word] += 1

        # it's possible that whole list has the same words
        buckets = [[] for i in range(len(words) + 1)]
        for word, count in countMap.items():
            buckets[count].append(word)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            if buckets[i]:
                buckets[i].sort()
            for word in buckets[i]:
                res.append(word)

                if len(res) == k:
                    return res

        return res
        