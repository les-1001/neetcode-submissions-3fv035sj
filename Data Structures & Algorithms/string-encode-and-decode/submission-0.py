class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello", "World"]
        # "5#Hello5#World"
        ans = ""
        
        for s in strs:
            ans += str(len(s)) + "#" + s
        
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []

        # "10#HelloHello5#World"
        # 

        i = 0
        while i < len(s):
            start = i
            while s[start] != "#":
                start += 1
            length = int(s[i:start])
            ans.append(s[start + 1: start + length + 1])
            i = start + length + 1

        return ans