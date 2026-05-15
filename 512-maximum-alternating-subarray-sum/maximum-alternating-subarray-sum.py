class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        curOddSum = nums[0]
        curEvenSum = float("-inf")
        maxSum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # even length
            nextEvenSum = curOddSum - num
            # odd length
            nextOddSum = max(num, curEvenSum + num)

            curEvenSum = nextEvenSum
            curOddSum = nextOddSum

            maxSum = max(maxSum, curEvenSum, curOddSum)

        return maxSum
        