# 面试题61. 扑克牌中的顺子

class Solution:
    def isStraight(self, nums) -> bool:
        nums.sort()
        numZeros = nums.count(0)
        if len(set(nums[numZeros:])) < len(nums[numZeros:]): return False
        return nums[-1] - nums[numZeros] <= 4