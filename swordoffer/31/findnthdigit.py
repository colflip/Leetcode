from bisect import bisect_left


class Solution:
    def findNthDigit(self, n: int) -> int:
        if not n: return 0
        n -= 1
        f = lambda x: ((9 * x + 8) * 10 ** (x + 1) + 1) // 9
        i = bisect_left(range(-1, 8), 1, key=lambda x: f(x) > n)
        d, r = divmod(n - f(i - 1), i)
        return (10 ** i + d) // 10 ** (i - r - 1) % 10
