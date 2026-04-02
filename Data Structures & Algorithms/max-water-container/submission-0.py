class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        volume = 0

        while l < r:
            height = min(heights[l], heights[r])
            volume = max(volume, (r - l) * height)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        
        return volume