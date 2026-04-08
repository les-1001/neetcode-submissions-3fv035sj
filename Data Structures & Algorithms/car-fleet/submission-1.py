class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = sorted(([p, s] for p, s in zip(position, speed)), reverse=True)
        output = []

        for p, s in pos:
            time = (target - p) / s
            if not output or output[-1] < time:
                output.append(time)

        return len(output)