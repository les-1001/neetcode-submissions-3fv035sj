class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1 = sorted(s1)

        for i in range(len(s2)):
            for j in range(i, len(s2)):
                curr = sorted(s2[i : j + 1])
                if curr == s1:
                    return True

        return False