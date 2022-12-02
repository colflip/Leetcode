# 剑指 Offer 40. 最小的k个数


class Solution:
    def getLeastNumbers(self, arr, k: int):
        return sorted(arr)[:k]


arr = [3, 2, 1]
k = 2
print(Solution().getLeastNumbers(arr, k))
