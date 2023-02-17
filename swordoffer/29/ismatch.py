# 剑指 Offer 19. 正则表达式匹配

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True

        for j in range(2, n):
            if p[j - 1] == '*' and p[j - 2] != '*':
                dp[0][j] = dp[0][j - 2]

        if m > 1 and n > 1:
            dp[1][1] = s[0] == p[0] or p[0] == '.'

        for i in range(1, m):
            for j in range(2, n):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[i][j] = False
        return dp[m - 1][n - 1]
