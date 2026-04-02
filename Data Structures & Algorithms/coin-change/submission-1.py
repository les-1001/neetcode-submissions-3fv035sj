class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for num in coins:
            for i in range(1, amount+1):
                if i == num:
                    dp[i] = min(dp[i], dp[i - 1] + 1)
                if i >= num:
                    dp[i] = min(dp[i], dp[i-num] + 1)

        return -1 if dp[-1] == amount + 1 else dp[-1]