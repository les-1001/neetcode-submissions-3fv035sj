class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30, 38, 30, 36, 35, 40, 28]
        # res = [0, 0, 0, 0, 0, 0, 0]
        # stack = [(30, 0), ]
        # temp = 30, index = 0
        output = [0] * len(temperatures)
        check = []

        for i, t in enumerate(temperatures):
            while check and t > temperatures[check[-1]]:
                index = check.pop()
                output[index] = i - index
            check.append(i)

        return output
    