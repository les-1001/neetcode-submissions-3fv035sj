class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = sorted( ([p, s] for p, s in zip(position, speed)), reverse=True)

        ans = []
        for p, s in pos:
            time_taken = (target - p) / s
            if not ans or ans[-1] < time_taken:
                ans.append(time_taken)

        return len(ans)