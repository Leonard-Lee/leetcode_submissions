class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        def helper(subnums) -> int:
            m = len(subnums)
            if m == 0:
                return 0
            elif m == 1:
                return subnums[0]
                
            res = [0] * m
            res[0] = subnums[0]
            res[1] = max(subnums[1], res[0])

            for i in range(2, m):
                res[i] = max(res[i - 1], subnums[i] + res[i - 2])

            return res[-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
        
        