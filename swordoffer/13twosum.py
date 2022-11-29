# 剑指 Offer 57.和为s的两个数字

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            sum = nums[l] + nums[r]
            if sum == target:
                return [nums[l], nums[r]]
            elif sum > target:
                r -= 1
            else:
                l += 1
        return []
