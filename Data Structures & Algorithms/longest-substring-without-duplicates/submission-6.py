class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        count = 1

        for i in range(len(s) - 1):
            seen = set()
            seen.add(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    count = max(count, len(seen))
                else:
                    break
        return count