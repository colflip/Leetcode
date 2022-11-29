# 剑指 Offer 11. 旋转数组的最小数字

class Solution:
    def minArray(self, numbers) -> int:
        temp = numbers[0]
        for i in numbers:
            if i < temp:
                return i
        return temp

        # -------------------------------
        # return min(numbers)


numbers = [3, 4, 5, 1, 2]
print(Solution().minArray(numbers))
