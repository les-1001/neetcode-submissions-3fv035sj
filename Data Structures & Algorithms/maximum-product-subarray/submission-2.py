class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_num = nums[0]
        max_num = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            prev_min, prev_max = min_num, max_num
            min_num = min(nums[i], prev_min * nums[i], prev_max * nums[i])
            max_num = max(nums[i], prev_min * nums[i], prev_max * nums[i])
            res = max(res, min_num, max_num)
        
        return res