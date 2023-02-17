# 1545. 找出第 N 个二进制字符串中的第 K 位

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        lens = {1: 1}
        sum = 1
        for i in range(2, n + 1):
            sum = 2 * sum + 1
            lens[i] = sum

        def process(n, k):
            if n == 1:
                return '0'
            mid = lens[n] // 2 + 1
            if k == mid:
                return "1"
            elif k < mid:
                return process(n - 1, k)
            else:
                return '0' if process(n - 1, lens[n - 1] - (k - mid) + 1) == '1' else '1'

        return process(n, k)
