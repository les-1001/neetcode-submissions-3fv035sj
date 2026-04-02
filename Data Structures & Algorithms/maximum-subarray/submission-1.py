class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                largest = max(largest, sum(nums[i:j + 1]))
        return largest