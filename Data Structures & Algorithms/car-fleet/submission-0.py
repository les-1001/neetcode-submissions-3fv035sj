class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = []
        n = len(position)

        for i in range(n):
            pos.append((position[i], speed[i]))

        pos = sorted(pos, key=lambda x: x[0], reverse=True)

        time = []
        for p, t in pos:
            time_taken = (target - p) / t
            if not time or time[-1] < time_taken:
                time.append(time_taken)

        return len(time)