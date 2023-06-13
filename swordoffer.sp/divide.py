"""
divide-two-integers
https://leetcode-cn.com/problems/divide-two-integers/
"""


class Solution:
    def divide(self, a: int, b: int) -> int:
        ret = 0
        flag = False if (a > 0 and b > 0) or (a < 0 and b < 0) else True
        a, b = abs(a), abs(b)

        def calc(x, y):
            n = 1
            while x > y << 1:
                y <<= 1
                n <<= 1
            return n, y

        while a >= b:
            cnt, val = calc(a, b)
            ret += cnt
            a -= val
        ret = -ret if flag else ret
        return ret - 1 if ret >= 2 ** 31 else ret


if __name__ == "__main__":
    a = 15
    b = 2
    s = Solution()
    print(s.divide(a, b))
