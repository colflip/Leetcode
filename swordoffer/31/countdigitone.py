class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        t = 1
        for i in range(len(str(n)) - 1, 0, -1):
            num = 10 ** i
            a = n // num
            if a > t:
                ans += num
            elif a == t:
                ans += n - num + 1
            while n > num:
                ans += i * num // 10
                n -= num
        return ans + (n >= t)
