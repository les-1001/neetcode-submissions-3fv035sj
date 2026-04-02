class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        stack = Counter(nums)
        sort_keys = sorted(stack.keys(), key=lambda x: stack[x],reverse=True)
        ans = []
        for i in sort_keys:
            if len(ans) < k:
                ans.append(i)
            else:
                return ans
        return ans