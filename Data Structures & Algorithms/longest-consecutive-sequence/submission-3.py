class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0

        for num in nums:
            if num - 1 not in nums:
                curr = 0
                while (num + curr) in nums:
                    curr += 1
                ans = max(ans, curr)
        
        return ans