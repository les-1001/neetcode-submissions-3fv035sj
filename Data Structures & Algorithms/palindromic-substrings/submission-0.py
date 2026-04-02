class Solution:
    def countSubstrings(self, s: str) -> int:
        odd = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                odd += 1
                l -= 1
                r += 1

        even = 0
        for i in range(len(s)):
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                even += 1
                l -= 1
                r += 1

        return odd + even