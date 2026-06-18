class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            tmp = temperatures[i]

            while stack and stack[-1][0] < tmp:
                oldTemp, idx = stack.pop()
                res[idx] = i - idx 

            stack.append([tmp, i])

        return res
        