class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        check = []

        for i, t in enumerate(temperatures):
            while check and t > check[-1][0]:
                temp, index = check.pop()
                result[index] = i - index
            check.append((t, i))
        
        return result