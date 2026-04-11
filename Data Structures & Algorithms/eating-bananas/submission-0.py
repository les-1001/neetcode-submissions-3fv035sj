class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            mid = (l + r) // 2
            time = 0
            for num in piles:
                time += 1 + (num // mid)
            if time <= h:
                k = min(k, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return k

    