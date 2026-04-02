class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        rob1, rob2 = 0, 0
        for i in range(len(nums)-1):
            curr = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = curr
        
        rob3, rob4 = 0, 0
        for i in range(1, len(nums)):
            curr = max(rob3 + nums[i], rob4)
            rob3 = rob4
            rob4 = curr
        
        return max(rob2, rob4)