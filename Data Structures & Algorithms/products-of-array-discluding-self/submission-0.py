class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero = 1, 0
        n = len(nums)
        output = [0] * n

        for num in nums:
            if num == 0:
                zero += 1
                if zero > 1:
                    return output
            else:
                prod *= num
        
        for i in range(n):
            if zero:
                if nums[i] == 0:
                    output[i] = prod
                    return output
            else:
                output[i] = prod // nums[i]
        return output           