# 46. 把数字翻译成字符串

class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1

        nums = str(num)
        dp = [1] * len(nums)
        dp[1] = 2 if 9 < nums[:2] < 26 else 1

        for i in range(2, len(nums)):
            dp[i] = dp[i - 1] + dp[i - 2] if 9 < num[i - 1:i + 1] < 26 else dp[i - 1]
        return dp[-1]


num = 12258
print(Solution().translateNum(num))
