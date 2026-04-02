class Solution:
    def climbStairs(self, n: int) -> int:
        one, two, curr = 1, 1, 0
        for i in range(n-1):
            curr = one + two
            one = two
            two = curr       
        return two