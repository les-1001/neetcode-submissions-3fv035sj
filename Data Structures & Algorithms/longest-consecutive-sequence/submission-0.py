class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 1
        curr = 1
        print(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                res = max(res, curr)
                curr = 1
        res = max(res, curr)

        return res