class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        n = len(temperatures)
        stack = []
        res = [0] * n
        for i in range(n):
            tmp = temperatures[i]

            while stack and temperatures[stack[-1]] < tmp:
                idx = stack.pop()
                res[idx] = i - idx 

            stack.append(i)

        return res
        