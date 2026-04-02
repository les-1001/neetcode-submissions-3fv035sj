class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for left, right in intervals:
            prev = ans[-1][1]
            if left <= prev:
                ans[-1][1] = max(prev, right)
            else:
                ans.append([left, right])
        return ans