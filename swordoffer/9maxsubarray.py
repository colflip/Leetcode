# 42. 连续子数组的最大和


class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(Solution().maxSubArray(nums))
