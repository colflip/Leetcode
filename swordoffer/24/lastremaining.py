# 剑指 Offer 62. 圆圈中最后剩下的数字


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        p = 0
        for i in range(2, n + 1):
            p = (p + m) % i
        return p


if __name__ == "__main__":
    n, m = 70866, 116922
    solution = Solution()
    print(solution.lastRemaining(n, m))
