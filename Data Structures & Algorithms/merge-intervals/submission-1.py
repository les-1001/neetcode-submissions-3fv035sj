class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for l, r in intervals:
            right = ans[-1][1]
            if l <= right:
                ans[-1][1] = max(right, r)
            else:
                ans.append([l, r])
        return ans