class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [0, 1, 1]
        for i in range(3, n + 1):
            res = 0
            for j in range(1, i):
                res = max(res, max(j * (i - j), j * dp[i - j]))
            dp.append(res)
        return dp[n] % 1000000007


# class Solution:
#     def cuttingRope(self, n: int) -> int:
#         _mod = 1000000007
#         if n == 2:
#             return 1
#         elif n == 3:
#             return 2
#         elif n == 4:
#             return 4
#         elif n % 3 == 1:
#             ans = 4
#             x = n // 3
#             for i in range(1, x):
#                 ans *= 3
#                 while ans >= _mod:
#                     ans -= _mod
#         elif n % 3 == 2:
#             ans = 2
#             x = n // 3
#             for i in range(x):
#                 ans *= 3
#                 while ans >= _mod:
#                     ans -= _mod
#         else:
#             ans = 1
#             x = n // 3
#             for i in range(x):
#                 ans *= 3
#                 while ans >= _mod:
#                     ans -= _mod
#
#         return ans
