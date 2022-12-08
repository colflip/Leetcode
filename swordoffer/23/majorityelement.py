# 剑指 Offer 39. 数组中出现次数超过一半的数字

class Solution:
    def majorityElement(self, nums) -> int:
        return sorted(nums)[len(nums) // 2]


nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
print(Solution().majorityElement(nums))
