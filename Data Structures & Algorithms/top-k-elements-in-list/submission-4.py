class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for v, i in Counter(nums).most_common(k):
            ans.append(v)
        return ans