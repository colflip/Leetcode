# 剑指 Offer 57 - II. 和为s的连续正数序列

class Solution:
    def findContinuousSequence(self, target: int) -> list:
        n = 2
        result = []
        while (n * n // 2) <= target:
            if target % n == 0:
                left = target // n - n // 2
            else:
                left = target // n - n // 2 + 1

            right = left + n - 1
            if (left + right) * n == target * 2:
                result.insert(0, list(range(left, right + 1)))
            n += 1
        return result


a = Solution()
print(a.findContinuousSequence(9))
print(a.findContinuousSequence(15))
