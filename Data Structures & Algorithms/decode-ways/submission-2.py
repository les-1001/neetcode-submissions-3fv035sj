class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        if int(s[-1]) != 0:
            dp[len(s)-1] = 1
        if s[0] == "0":
            return 0

        for i in range(len(s)-2, -1, -1):
            if int(s[i]) > 0:
                dp[i] += dp[i+1]
            if int(s[i]) != 0 and int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]

            print(dp)

        return dp[0]