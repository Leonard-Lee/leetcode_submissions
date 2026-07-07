class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums

        # i for even and j for odd
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2

        return nums
        