class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            find = target - num
            if find in seen:
                return [seen[find], i]
            seen[num] = i